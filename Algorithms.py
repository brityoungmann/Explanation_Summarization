import ast
import multiprocessing
import statistics
import Utils
import warnings
import Data2Transactions
import time
warnings.filterwarnings('ignore')
PATH = "./data/"
CPU_COUNT = 8


def filterPatterns(df, groupingAtt, groups):
    groups_dic = {}
    for group in groups:
        df['GROUP_MEMBER'] = df.apply(lambda row: isGroupMember(row, group), axis=1)
        df_g = df[df['GROUP_MEMBER'] == 1]
        covered = set(df_g[groupingAtt].tolist())
        groups_dic[str(group)] = frozenset(covered)
    from collections import defaultdict

    grouped = defaultdict(list)
    for key in groups_dic:
        grouped[groups_dic[key]].append(key)

    ans = []
    for k,v in grouped.items():
        if len(v) > 1:
            v = [ast.literal_eval(i) for i in v]
            ans.append(min(v, key=lambda x: len(x)))
        else:
            ans.append(ast.literal_eval(v[0]))
    return ans


def getAllGroups(df_org, atts, t):
    df = df_org.copy(deep=True)
    df = df[atts]
    df, rows, columns = Data2Transactions.removeHeader(df, 'Temp.csv')
    rules = Data2Transactions.getRules(df, rows, columns, min_support=t)
    return rules


def getGroupstreatments(DAG, df, groupingAtt, groups, ordinal_atts, targetClass,
                        high, low,actionable_atts, print_times, sample = False):
    manager = multiprocessing.Manager()
    groups_dic = manager.dict()
    elapsed_time = 0

    start_time = time.time()
    arg_list = [(group, df, groups_dic, groupingAtt, targetClass, DAG, ordinal_atts, high, low,
                 actionable_atts) for group in groups]
    # Create a non-daemonic process pool
    with multiprocessing.get_context('spawn').Pool() as pool:
        # Apply the update_dictionary function to each argument in parallel
        pool.starmap(process_group, arg_list)


    elapsed_time = time.time() - start_time

    if print_times:
        print(f"Elapsed time step 2: {elapsed_time} seconds")
    return groups_dic, elapsed_time



def process_group(group, df, groups_dic, groupingAtt, targetClass,
                   DAG, ordinal_atts, high, low,
    actionable_atts):


    df['GROUP_MEMBER'] = df.apply(lambda row: isGroupMember(row, group), axis=1)
    df_g = df[df['GROUP_MEMBER'] == 1]
    drop_atts = list(group.keys())
    drop_atts.append('GROUP_MEMBER')
    drop_atts.append(groupingAtt)
    # df_g = df_g.drop(drop_atts, axis = 1)

    covered = set(df_g[groupingAtt].tolist())

    #
    # # step 2 - top down algorithm
    #
    (t_h, cate_h), (t_l, cate_l) = getHighLowTreatments(df_g, group, targetClass,
                                                         DAG, drop_atts,
                                                        ordinal_atts, high, low, actionable_atts)


    epxlainability = getExp(cate_h, cate_l, high, low)

    groups_dic[str(group)] = [len(df_g), covered, t_h, cate_h, t_l, cate_l, epxlainability]



def getExp(cate_h, cate_l, high, low):
    if high and low:
        return sum([abs(cate_h), abs(cate_l)])
    elif high:
        return cate_h
    else:
        return abs(cate_l)


def isGroupMember(row, group):
    for att in group:
        column_c_type = type(row[att])
        if type(row[att]) == int:
            if not row[att] == int(group[att]):
                return 0
        elif type(row[att]) == str:
            if row[att] == group[att]:
                return 1
            else:
                return 0
        elif int(row[att]) == int(group[att]):
                return 1
        elif not row[att] == group[att]:
            return 0
    return 1


def getHighLowTreatments(df_g, group, target,DAG, dropAtt, ordinal_atts, high, low,actionable_atts_org):
    df_g.drop(dropAtt, axis=1, inplace=True)
    actionable_atts = [a for a in actionable_atts_org if not a in dropAtt]
    df_g = df_g.loc[:, ~df_g.columns.str.contains('^Unnamed')]
    # cols = df_g.columns
    # cols = cols.drop(target)
    print('starting group: ', group)
    treatments = Utils.getLevel1treatments(actionable_atts, df_g, ordinal_atts)
    print('num of treatments at level I: ', len(treatments))

    t_h = None
    cate_h = 0
    t_l = None
    cate_l = 0
    treatments_cate, t_h, cate_h, t_l,cate_l = Utils.getCates(DAG,t_h,t_l, cate_h, cate_l, df_g,
                                                              ordinal_atts, target, treatments)

    treatments_cate = filter_above_below_median(treatments_cate)

    treatments = Utils.getNextLeveltreatments(treatments_cate, df_g, ordinal_atts, high, low)
    print('num of treatments at level II: ', len(treatments))
    #print(treatments)
    treatments_cate, t_h2, cate_h2, t_l2, cate_l2 = Utils.getCates(DAG,t_h,t_l, cate_h, cate_l, df_g, ordinal_atts, target,
                                                             treatments)
    if high:
        if t_h2 != t_h:
            print("high treatment found in level 2")
            t_h = t_h2
            cate_h = cate_h2
    if low:
        if t_l2 != t_l:
            print("low treatment found in level 2")
            t_l = t_l2
            cate_l = cate_l2

    # TODO: support upper levels
    print('finished group: ', group)
    print(t_h, cate_h)
    print(t_l, cate_l)
    print('#######################################')
    return (t_h, cate_h), (t_l, cate_l)


def filter_above_below_median(data):
    # Extract the values from the dictionary
    values = list(data.values())

    # Separate positive and negative values
    positive_values = [value for value in values if value > 0]
    negative_values = [value for value in values if value < 0]

    # Calculate the positive median and negative median
    positive_median = statistics.median(positive_values) if positive_values else None
    negative_median = statistics.median(negative_values) if negative_values else None

    # Filter the dictionary entries
    filtered_data = {key: value for key, value in data.items()
                     if (value > positive_median and value > 0) or (value < negative_median and value < 0)}

    return filtered_data


