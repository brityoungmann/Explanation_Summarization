import random
from dowhy import CausalModel
import warnings
warnings.filterwarnings('ignore')
from itertools import chain, combinations
from itertools import product
import ast
from z3 import *
THRESHOLD = 0.8

def getRandomTreatment(atts, df):
    ans = {}
    k = random.randrange(1, len(atts))
    selectedAtts = random.sample(atts, k)

    for a in selectedAtts:
        val = random.choice(list(set(df[a].tolist())))
        ans[a] = val
    df['TempTreatment'] = df.apply(lambda row: addTempTreatment(row, ans), axis=1)
    print(df['TempTreatment'].value_counts())
    valid = list(set(df['TempTreatment'].tolist()))
    # no tuples in treatment group
    if len(valid) < 2:
        return None
    return ans, df

def getAllTreatments(atts, df):
    ans = []
    atts_vals = getAttsVals(atts,df)

    for selectedAtts in chain.from_iterable(combinations(atts, r) for r in range(len(atts)+1)):
        if len(selectedAtts) == 0:
            continue
        dict_you_want = {your_key: atts_vals[your_key] for your_key in selectedAtts}
        keys, values = zip(*dict_you_want.items())
        permutations_dicts = [dict(zip(keys, v)) for v in product(*values)]
        for p in permutations_dicts:
            df['TempTreatment'] = df.apply(lambda row: addTempTreatment(row, p), axis=1)
            valid = list(set(df['TempTreatment'].tolist()))
            # no tuples in treatment group
            if len(valid) < 2:
                continue
            #print(p)
            ans.append(p)
    print("number of patterns to consider: ", len(ans))
    return ans



def countHighLow(df, bound, att):
    vals = df[att].tolist()

    high = 0
    low = 0
    for v in vals:
        if v >= bound:
            high = high + 1
        else:
            low = low + 1
    return high,low

def getAttsVals(atts,df):
    ans = {}
    for a in atts:
        vals = list(set(df[a].tolist()))
        ans[a] = vals
    return ans


def getNextLeveltreatments(treatments_cate, df_g, ordinal_atts, high, low):
    treatments = []
    if high:
        positives = getTreatmeants(treatments_cate, 'positive')
    if low:
        negatives = getTreatmeants(treatments_cate, 'negative')
    if high:
        treatments = getCombTreatments(df_g, positives, treatments, ordinal_atts)
    if low:
        treatments = getCombTreatments(df_g, negatives, treatments, ordinal_atts)
    return treatments


def getCombTreatments(df_g, positives, treatments, ordinal_atts):
    for comb in combinations(positives, 2):
        t = copy.deepcopy(comb[1])
        t.update(comb[0])
        if len(t.keys()) == 2:

            df_g['TempTreatment'] = df_g.apply(lambda row: addTempTreatment(row, t, ordinal_atts), axis=1)
            valid = list(set(df_g['TempTreatment'].tolist()))
            # no tuples in treatment group
            if len(valid) < 2:
                continue
            size = len(df_g[df_g['TempTreatment'] == 1])
            # treatment group is too big or too small
            if size > 0.9 * len(df_g) or size < 0.1 * len(df_g):
                continue
            treatments.append(t)

    return treatments

def getLevel1treatments(atts, df,ordinal_atts):
    ans = []
    atts_vals = getAttsVals(atts,df)

    count = 0
    for att in atts_vals:
        for val in atts_vals[att]:
            p = {att:val}
            df['TempTreatment'] = df.apply(lambda row: addTempTreatment(row, p, ordinal_atts), axis=1)
            valid = list(set(df['TempTreatment'].tolist()))
            # no tuples in treatment group
            if len(valid) < 2:
                continue
            size = len(df[df['TempTreatment'] == 1])
            count=count+1
            # treatment group is too big or too small
            if size > 0.9*len(df) or size < 0.1*len(df):
                continue
            ans.append(p)
    return ans

def getTreatmeants(treatments_cate, bound):
    #import ast
    ans = []
    for k,v in treatments_cate.items():
        if bound == 'positive':
            if v > 0:
                ans.append(ast.literal_eval(k))
        if bound == 'negative':
            if v < 0:
                ans.append(ast.literal_eval(k))
    return ans

def getCates(DAG, t_h,t_l,cate_h, cate_l, df_g, ordinal_atts, target, treatments):
    treatments_cate = {}
    for treatment in treatments:
        CATE = getTreatmentCATE(df_g, DAG, treatment, ordinal_atts, target)
        if CATE == 0:
            continue
        treatments_cate[str(treatment)] = CATE
        if CATE > cate_h:
            cate_h = CATE
            t_h = treatment
        if CATE < cate_l:
            cate_l = CATE
            t_l = treatment
    return treatments_cate, t_h, cate_h, t_l,cate_l

def getTreatmentCATE(df_g, DAG,treatment,ordinal_atts,target):
    df_g['TempTreatment'] = df_g.apply(lambda row: addTempTreatment(row, treatment, ordinal_atts), axis=1)
    DAG_ = changeDAG(DAG, treatment)
    causal_graph = """
                        digraph {
                        """
    for line in DAG_:
        causal_graph = causal_graph + line + "\n"
    causal_graph = causal_graph + "}"
    try:
        ATE, p_value = estimateATE(causal_graph, df_g, 'TempTreatment', target)
        if p_value > THRESHOLD:
            ATE = 0
    # print(treatment, c, ATE, p_value)
    except:
        ATE = 0
        p_value = 0
    return ATE


def addTempTreatment(row, ans, ordinal_atts):
    for a in ans:
        if a in ordinal_atts:
            index = ordinal_atts[a].index(ans[a])
            index_i = ordinal_atts[a].index(row[a])
            if index_i < index:
                return 0
        else:
            if not row[a] == ans[a]:
                return 0
    return 1

def changeDAG(dag, randomTreatment):
    DAG = copy.deepcopy(dag)
    toRomove = []
    toAdd = ['TempTreatment;']
    for a in randomTreatment:
        for c in DAG:
            if '->' in c:
                if a in c:
                    toRomove.append(c)
                    # left hand side
                    if c.find(a) == 0:
                        string = c.replace(a, "TempTreatment")
                        if not string in toAdd:
                            toAdd.append(string)
                        # str = a + " -> TempTreatment"
                        # if not str in toAdd:
                        #     toAdd.append(str)
                    # right hand side
    for r in toRomove:
        if r in DAG:
            DAG.remove(r)
    for a in toAdd:
        if not a in DAG:
            DAG.append(a)
    return list(set(DAG))

def estimateATE(causal_graph, df, T, O):
    model = CausalModel(
        data=df,
        graph=causal_graph.replace("\n", " "),
        treatment=T,
        outcome=O)

    #model.view_model()
    # print("*****************DEBUG********************88")
    # print(causal_graph)
    #
    # print("*****************DEBUG********************88")
    # Identify the causal effect
    estimands = model.identify_effect()

    causal_estimate_reg = model.estimate_effect(estimands,
                                                method_name="backdoor.linear_regression",
                                                target_units="ate",
                                                #evaluate_effect_strength=True,
                                                effect_modifiers = [],
                                                test_significance=True)
    return causal_estimate_reg.value, causal_estimate_reg.test_stat_significance()['p_value']


def graph(df, x, y):
    X = df[x].tolist()
    Y = df[y].tolist()


def displayGraph():
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph()
    # G.add_edges_from(
    #     [
    #         ('Gender', 'FormalEducation'),
    #         ('Gender','UndergradMajor'),
    #         ('Gender','DevType'),
    #         ('Gender','YearsCoding'),
    #          ('Gender','ConvertedSalary'),
    #          ('Country','ConvertedSalary'),
    #          ('Country', 'FormalEducation'),
    #          ('Country','RaceEthnicity'),
    #           ('Country','YearsCoding'),
    #            ('Country','EducationParents'),
    #          ('FormalEducation','DevType'),
    #          ('FormalEducation', 'UndergradMajor'),
    #          ('FormalEducation','YearsCoding'),
    #          ('EducationParents','UndergradMajor'),
    #          ('EducationParents','FormalEducation'),
    #          ('RaceEthnicity','ConvertedSalary'),
    #          ('RaceEthnicity', 'UndergradMajor'),
    #          ('RaceEthnicity','YearsCoding'),
    #          ('RaceEthnicity','EducationParents'),
    #          ('UndergradMajor','DevType'),
    #          ('UndergradMajor', 'YearsCoding'),
    #          ('YearsCoding','ConvertedSalary'),
    #          ('DevType','ConvertedSalary'),
    #          ('DevType','HoursComputer'),
    #          ('Age','ConvertedSalary'),
    #          ('Age', 'DevType'),
    #          ('Age','YearsCoding'),
    #          ('Age','FormalEducation'),
    #          ('HoursComputer','ConvertedSalary')])

    G.add_edges_from(
        [
            ('MONTH', 'WEATHER'),
            ('MONTH', 'DEPARTURE_DELAY'),
            ('MONTH', 'City'),
            ('AIRLINE', 'DEPARTURE_DELAY'),
            ('ORIGIN_AIRPORT', 'AIRLINE'),
            ('City', 'WEATHER'),
            ('City', 'ORIGIN_AIRPORT'),
            ('City', 'POPULATION'),
            ('ORIGIN_AIRPORT', 'DEPARTURE_DELAY'),
            ('WEATHER', 'DEPARTURE_DELAY'),
            ('WEATHER', 'SNOW'),
            ('SNOW', 'DEPARTURE_DELAY'),
            ('POPULATION', 'DEPARTURE_DELAY')

        ])

    print(nx.is_directed_acyclic_graph(G))

    pos = nx.circular_layout(G)
    # nx.draw_networkx_nodes(G, pos, label=True, node_size=500)
    nx.draw(G,pos=pos, with_labels=True)

    plt.show()


def LPSolver(groups_dic, k, tau, m):
    groups = groups_dic.keys()
    universe = set()
    for key, v in groups_dic.items():
        universe.update(v[1])

    print("sets: ", len(groups), "universe: ", len(universe))
    sets_dic = {}
    sets = []
    # Create a Z3 optimizer
    opt = Optimize()
    i = 0
    for g in groups:
        name = "g"+str(i)
        name = BitVec(name, 1)
        opt.add(Or(name == 1, name == 0))
        sets_dic[g] = name
        sets.append(name)
        i = i +1
    elements_dic = {}
    i = 0
    for e in universe:
        name = "e"+str(i)
        name = BitVec(name, 1)
        i = i +1
        elements_dic[e] = name

    # # Add the constraint that restricts no more than k variables to be 1
    opt.add(PbLe([(var, 1) for var in sets], k))

    # Define objective (example: maximize the sum of variables)
    objective = Sum(sets)
    opt.maximize(objective)

    # Solve the optimization problem
    result = opt.check()

    if result == sat:
        model = opt.model()
        values = [model.evaluate(sets[i]) for i in range(len(sets))]
        for i in range(len(sets)):
            print('x{} = {}'.format(i + 1, values[i].as_long()))
        print('Objective value:', model.evaluate(objective))
    elif result == unsat:
        print('No solution found.')
    else:
        print('Optimization problem is either unknown or not supported.')

    return groups, 0, 0



def LP_solver(sets, weights, tau, k, m):
    # for s in sets:
    #     print(sets[s], weights[s])
    solver = Optimize()

    # Create a boolean variable for each set
    set_vars = {name: Bool(name) for name in sets}

    # # Add the constraint that at most k sets can be selected
    solver.add(Sum([set_vars[name] for name in sets]) <= k)

    # Add the constraint that at least tau fraction of all elements must be covered
    elements = set.union(*[set(sets[name]) for name in sets])
    # print(elements)
    # print(tau, m, tau*m)
    element_covered = [Bool(f"Element_{element}") for element in elements]
    for i, element in enumerate(elements):
        solver.add(Implies(element_covered[i], Or([set_vars[name] for name in sets if element in sets[name]])))
        # covered_sets = [set_vars[name] for name in sets if element in sets[name]]
        # solver.add(element_covered[i] <= Sum(covered_sets))


    solver.add(Sum(element_covered) >= (tau * m))

    # Maximize the sum of weights
    solver.maximize(Sum([set_vars[name] * weights[name] for name in sets]))

    # Check for satisfiability and retrieve the optimal solution
    if solver.check() == sat:
        model = solver.model()
        selected_sets = [name for name in sets if is_true(model[set_vars[name]])]
        return selected_sets
    else:
        print("no solution was found!")
        return []
