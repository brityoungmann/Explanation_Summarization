import pandas as pd
from apyori import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


def addColName(row, col):
    val = row[col]
    return col +" = "+str(val)

def removeHeader(df_org, name):
    df = df_org.copy(deep = True)
    columns = df.columns
    for col in columns:
        df[col] = df.apply(lambda row: addColName(row, col), axis=1)

    # rows_to_add = []
    # for index, row in df.iterrows():
    #     for att in ordinal_atts:
    #         val = row[att]
    #         val = val.split('=')[1].strip()
    #         index = ordinal_atts[att].index(val)
    #         for i in range(index+1, len(ordinal_atts[att])):
    #             implied_val = ordinal_atts[att][i]
    #             new_row = row.copy(deep = True)
    #             new_row[att] = implied_val
    #             rows_to_add.append(new_row)
    # print('before implied rows: ', len(df))
    # for row in rows_to_add:
    #     df.loc[len(df)] = row
    # print('after implied rows: ', len(df))
    df.to_csv(name, header=None, index=False)

    df = pd.read_csv(name, header=None)
    rows = len(df)
    columns = len(df.columns)
    print("size of df: ",rows, columns)
    return df, rows, columns



def all_equal_ivo(lst):
    return not lst or lst.count(lst[0]) == len(lst)

def aggregateColumn(att, g,k):
    vals = g[att].tolist()
    if all_equal_ivo(vals):
        return vals[0]
    else:
        return 'NotAllEqual'


def getRules(df, rows, columns,min_support):
    records = []
    for i in range(0, rows):
        records.append([str(df.values[i, j]) for j in range(0, columns)])

    print("num of records: ", len(records))

    te = TransactionEncoder()

    te_ary = te.fit(records).transform(records)

    df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

    rules = []
    #print(frequent_itemsets)
    for index, row in frequent_itemsets.iterrows():
        parts = set(row["itemsets"])
        temp = {}
        for part in parts:
            part = part.split("=")
            temp[part[0].strip()] = part[1].strip()
        rules.append(temp)
    return rules





