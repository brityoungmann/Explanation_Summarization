import Utils
import warnings
import Algorithms
warnings.filterwarnings('ignore')
PATH = "./data/"
import time
APRIORI = 0.1

def cauSumX(df,DAG, ordinal_atts,targetClass, groupingAtt, fds,k, tau,actionable_atts, high, low , print_times = False):

    df = df.dropna()
    #num of groups in the aggregated view
    m = len(df.groupby([groupingAtt]))

    # step 1 - Aprioiri algorithm
    if print_times:
        start_time = time.time()
    groups = Algorithms.getAllGroups(df, fds, APRIORI)

    print('num of groups: ', len(groups))
    groups = Algorithms.filterPatterns(df, groupingAtt, groups)
    print('num of groups after filtering: ', len(groups))
    if print_times:
        elapsed_time = time.time() - start_time
        #print(f"Elapsed time step 1: {elapsed_time} seconds")
        t1 = elapsed_time

    print(groups)
    #
    groups_dic, t2 = Algorithms.getGroupstreatments(DAG, df, groupingAtt, groups, ordinal_atts,
                                                 targetClass, high, low, actionable_atts, print_times)
    #
    # # # # step 3 -
    start_time = time.time()

    groups = {}
    weights = {}
    for group in groups_dic:
        groups[group] = groups_dic[group][1]
        weights[group] = groups_dic[group][6]
    sol = Utils.LP_solver(groups, weights, tau, k, m)

    print("##############solution##################")
    exp = 0
    coverage = set()
    for s in sol:
        e = groups_dic[s][6]
        exp = exp + e
        coverage.update(groups_dic[s][1])
        print(s, groups_dic[s])
    print("overall explainability: ", exp)
    print("coverage: ", len(coverage) / m, len(coverage), m)

    if print_times:
        elapsed_time = time.time() - start_time
        #print(f"Elapsed time step 3: {elapsed_time} seconds")
        t3 = elapsed_time
    return t1, t2, t3, t1+t2+t3