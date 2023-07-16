import pandas as pd
from apyori import apriori
salary_bound =  95780
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from collections import Counter
from statistics import mean


def salary(row):
    val = row['ConvertedSalary']
    if val >= salary_bound:
        return 'high'
    return 'low'

def dependents(row):
    val = row[  'Dependents']

    if val == "Yes":
        return "kids"
    return "no kids"

def preprocessSO(df,targetClass, keepClass = False):

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.fillna('UNKNOWN')

    df = df.drop([  'YearsCoding', 'HoursComputer', 'Exercise','SexualOrientation', 'EducationParents'], axis=1)

    df['Dependents'] =  df.apply(lambda row: dependents(row), axis=1)
    # df['Salary'] = df.apply(lambda row: salary(row), axis=1)
    df = df.drop(['Age', 'Respondent', 'Hobby', 'Student', 'UndergradMajorCS'], axis=1)
    if not keepClass:
        df = df.drop([targetClass], axis = 1)
    #df = df.drop(['Dependents'], axis=1)
    return df


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

def aggregateSOFormalEdu(df):
    devTypes = df.groupby(["FormalEducation"])

    ans = {}

    Continent = []
    AgeGroup = []
    ConvertedSalary = []
    FormalEducation = []
    UndergradMajor = []
    Gender = []
    DevType = []
    RaceEthnicity = []
    Dependents = []
    Country = []
    for n, g in devTypes:

        FormalEducation.append(n)

        AgeGroup.append(aggregateColumn('AgeGroup', g, 1))
        DevType.append(aggregateColumn('DevType', g, 3))
        UndergradMajor.append(aggregateColumn('UndergradMajor', g, 3))
        Dependents.append(aggregateColumn('Dependents', g, 1))
        RaceEthnicity.append(aggregateColumn('RaceEthnicity', g, 3))
        Continent.append(aggregateColumn('Continent', g, 1))
        Gender.append(aggregateColumn('Gender', g, 1))
        Country.append(aggregateColumn('Country', g, 3))

        salary = g['ConvertedSalary'].tolist()
        salary = mean(salary)
        ConvertedSalary.append(salary)
    ans['AgeGroup'] = AgeGroup
    ans['Dependents'] = Dependents
    ans['UndergradMajor'] = UndergradMajor
    ans['FormalEducation'] = FormalEducation
    ans['ConvertedSalary'] = ConvertedSalary
    ans['Gender'] = Gender
    ans['DevType'] = DevType
    ans['Continent'] = Continent
    ans['RaceEthnicity'] = RaceEthnicity
    ans['Country'] = Country
    df = pd.DataFrame(ans, columns=ans.keys())
    return df


def all_equal_ivo(lst):
    return not lst or lst.count(lst[0]) == len(lst)

def aggregateColumn(att, g,k):
    vals = g[att].tolist()
    if all_equal_ivo(vals):
        return vals[0]
    else:
        return 'NotAllEqual'
    # age = Counter(age)
    # ans= age.most_common(k)
    # ans = [str(i[0]) for i in ans]
    # ans = '; '.join(ans)
    # return ans

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
        #print(str(row["itemsets"]) +"\t"+str(row["support"]))
        # rule = ', '.join(list(row["itemsets"]))
        # parts = rule.split(',')
        parts = set(row["itemsets"])
        temp = {}
        for part in parts:
            part = part.split("=")
            temp[part[0].strip()] = part[1].strip()
        rules.append(temp)
    return rules





