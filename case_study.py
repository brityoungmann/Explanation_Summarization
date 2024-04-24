import pandas as pd
import warnings
import random
warnings.filterwarnings('ignore')
PATH = "./data/"
import CPE
APRIORI = 0.1


def so(k, tau):
    #########################SO#####################
    'Hobby', 'Student',
    'FormalEducation', 'UndergradMajor', 'DevType', 'HoursComputer',
    'Exercise'
    actionable_atts = [
       'Gender', 'SexualOrientation', 'EducationParents', 'RaceEthnicity',
    'Age'
    ]
    DAG = [
        'Continent;',
        'HoursComputer;',
        'UndergradMajor;',
        'FormalEducation;',
        'Age;',
        'Gender;',
        'Dependents;',
        'Country;',
        'DevType;',
        'RaceEthnicity;',
        'ConvertedSalary;',
        'HDI;',
        'GINI;',
        'GDP;',
        'HDI -> GINI;',
        'GINI -> ConvertedSalary;',
        'GINI -> GDP;',
        'GDP -> ConvertedSalary;',
        'Gender -> FormalEducation;',
        'Gender -> UndergradMajor;',
        'Gender -> DevType;',
        'Gender -> ConvertedSalary;',
        'Country -> ConvertedSalary;',
        'Country -> FormalEducation;',
        'Country -> RaceEthnicity;',
        'Continent -> Country; '
    
        'FormalEducation -> DevType;',
        'FormalEducation -> UndergradMajor;',

        'Continent -> UndergradMajor',
        'Continent -> FormalEducation;',
        'Continent -> RaceEthnicity;',
        'Continent -> ConvertedSalary;',

        'RaceEthnicity -> ConvertedSalary;',
        'UndergradMajor -> DevType;',

        'DevType -> ConvertedSalary;',
        'DevType -> HoursComputer;',
        'Age -> ConvertedSalary;',
        'Age -> DevType;',
        'Age -> Dependents;',
        'Age -> FormalEducation;',

        'Dependents -> HoursComputer;',
        'HoursComputer -> ConvertedSalary;']

    df = pd.read_csv(PATH + 'so_countries_col_new.csv', encoding='utf8')
    ordinal_atts = {}
    targetClass = 'ConvertedSalary'
    groupingAtt = 'Country'
    fds = ['Country', 'GDP', 'HDI', 'GINI', 'Continent']
    #print(set(df['Continent'].tolist()))
    CPE.CPE(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
            print_times=True)


def german(k,tau):
    ####GERMAN############
    actionable_atts = ['status', 'duration', 'credit_history',
       'amount', 'savings', 'employment_duration', 'installment_rate',
       'personal_status_sex', 'other_debtors', 'present_residence', 'property',
       'age', 'other_installment_plans', 'housing', 'number_credits', 'job',
       'people_liable', 'telephone', 'foreign_worker']
    DAG = ['status;','duration;','credit_history;','purpose;','amount;','savings;',
        'employment_duration;','installment_rate;','personal_status_sex;','other_debtors;',
        'present_residence;','property;','age;','other_installment_plans;','housing;','number_credits;',
        'job;','people_liable;','telephone;','foreign_worker;','credit_risk;',
        'personal_status_sex -> credit_risk;','personal_status_sex -> housing;',
        'personal_status_sex -> savings;','personal_status_sex -> status;',
        'personal_status_sex -> credit_history;','personal_status_sex -> duration;',
        'personal_status_sex -> amount;','housing -> credit_risk;',
        'savings -> credit_risk;','status -> credit_risk;',
        'duration -> credit_risk;','credit_history -> credit_risk;',
        'amount -> credit_risk;','age -> credit_risk;',
        'age -> housing;','age -> credit_history;',
        'age -> savings;','age -> status;',
        'age -> duration;','age -> amount;']

    df = pd.read_csv(PATH + 'german_credit_data_new.csv', encoding='utf8')
    ordinal_atts = {}
    targetClass = 'credit_risk'
    groupingAtt = 'purpose'
    fds = ['purpose']
    CPE.CPE(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
            print_times=True)



def accidents(k,tau):
    ########Accidents###########
    DAG = [
        'Temperature -> Wind_Chill;',
        'Temperature -> Humidity;',
        'Temperature -> Weather_Condition;',
        'Wind_Chill -> Weather_Condition;',
        'Humidity -> Weather_Condition;',
        'Pressure -> Weather_Condition;',
        'Visibility -> Weather_Condition;',
        'Wind_Direction -> Wind_Speed;',
        'Wind_Speed -> Weather_Condition;',
        'Precipitation -> Weather_Condition;',
        'Amenity -> Traffic_Calming;',
        'Bump -> Traffic_Calming;',
        'Crossing -> Traffic_Signal;',
        'Give_Way -> Traffic_Signal;',
        'Junction -> Traffic_Signal;',
        'No_Exit -> Traffic_Signal;',
        'No_Exit -> Junction;',
        'Railway -> Traffic_Signal;',
        'Roundabout -> Traffic_Signal;',
        'Station -> Traffic_Signal;',
        'Station -> Crossing;',
        'Stop -> Traffic_Signal;',
        'Traffic_Signal -> Turning_Loop;',
        'Civil_Twilight -> Nautical_Twilight;',
        'Civil_Twilight -> Astronomical_Twilight;',
        'Nautical_Twilight -> Astronomical_Twilight;',
        'City -> Weather_Condition;',
        'State -> Weather_Condition;',
        'Region -> Weather_Condition;',

        'City -> Traffic_Signal;',
        'State -> Traffic_Signal;',
        'Region -> Traffic_Signal;',
        'City ->  Traffic_Calming;',
        'State ->  Traffic_Calming;',
        'Region ->  Traffic_Calming;',

        'Start_Time -> Weather_Condition;',
        'Start_Time -> Civil_Twilight;',
        'Weather_Condition -> Severity;',
        'Traffic_Signal -> Severity;',
        'Traffic_Calming -> Severity;',
        'Traffic_Signal -> Distance;',
        'Traffic_Calming -> Distance;',
        'Distance -> Severity;',
        'Side -> Severity;',
        'Civil_Twilight -> Severity;',
        'Nautical_Twilight -> Severity;',
    ]

    df = pd.read_csv(PATH + 'US_Accidents_binned_state.csv', encoding='utf8').sample(frac=0.1)
    df = df.rename(columns={'Distance(mi)': 'Distance', 'Temperature(F)': 'Temperature',
                            'Wind_Chill(F)': 'Wind_Chill', 'Humidity(%)': 'Humidity',
                            'Pressure(in)': 'Pressure', 'Visibility(mi)': 'Visibility',
                            'Wind_Speed(mph)': 'Wind_Speed', 'Precipitation(in)': 'Precipitation'})

    ordinal_atts = {}
    targetClass = 'Severity'
    groupingAtt = 'City'

    fds = ['City', 'County', 'State', 'Region']
    actionable_atts = ['Side', 'Temperature',
                       'Wind_Chill', 'Humidity', 'Pressure', 'Visibility',
                       'Wind_Direction', 'Wind_Speed', 'Precipitation',
                       'Weather_Condition',
                       'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset',
                       'Civil_Twilight']

    CPE.CPE(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
            print_times=True)


def adult(k,tau):
    DAG = [
        'age;',
        'workclass;',
        'fnlwgt;',
        'education;',
        'education.num;',
        'marital.status;',
        'occupation;',
        'relationship;',
        'race;',
        'sex;',
        'capital.gain;',
        'capital.loss;',
        'hours.per.week;',
        'native.country;',
        'income;',
        'occupation_category;',
        # A
        'sex -> income;',
        'race -> income;',
        # C
        'age -> income;',
        'native.country -> income;',
        # M
        'sex -> marital.status;',
        'race -> marital.status;',
        'age -> marital.status;',
        'native.country -> marital.status;',
        'marital.status -> income;',
        # L
        'marital.status -> education.num;',
        'sex -> education.num;',
        'race -> education.num;',
        'age -> education.num;',
        'native.country -> education.num;',
        'education.num -> income;',
        # R
        'hours.per.week -> income;',
        'occupation -> income;',
        'workclass -> income;',
        'education.num -> hours.per.week;',
        'education.num -> occupation;',
        'education.num -> workclass;',
        'marital.status -> hours.per.week;',
        'marital.status -> occupation;',
        'marital.status -> workclass;',
        'age -> hours.per.week;',
        'native.country -> hours.per.week;',
        'age -> occupation;',
        'native.country -> occupation;',
        'age -> workclass;',
        'native.country -> workclass;',
        'sex -> hours.per.week;',
        'sex -> occupation;',
        'sex -> workclass;',
        'race -> hours.per.week;',
        'race -> occupation;',
        'race -> workclass;'
    ]

    df = pd.read_csv(PATH + 'adult_new.csv', encoding='utf8')
    actionable_atts = [ 'age', 'workclass',  'education',
      'marital.status',
       'relationship', 'race', 'sex',
       'hours.per.week', 'native.country', 'income']

    ordinal_atts = {}
    targetClass = 'income'
    groupingAtt = 'occupation'
    groups = df.groupby([groupingAtt])

    fds = ['occupation',
           'occupation_category']
    CPE.CPE(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
            print_times=True)


def impus(k,tau):
    actionable_atts = ['RELATE', 'AGE', 'SEX', 'RACE', 'MARST', 'CITIZEN', 'EDUC',
       'WORKLY']
    DAG = [
        'AGE;',
        'CLASSWKR;',
        'EDUC;',
        'MARST;',
        'RELATE;',
        'RACE;',
        'SEX;',
        'WORKLY;',
        'CITIZEN;',
        'INCTOT;',

        # A
        'SEX -> INCTOT;',
        'RACE -> INCTOT;',
        # C
        'AGE -> INCTOT;',
        'CITIZEN -> INCTOT;',
        # M
        'SEX -> MARST;',
        'RACE -> MARST;',
        'AGE -> MARST;',
        'CITIZEN -> MARST;',
        'MARTST -> INCTOT;',
        # L
        'MARST -> EDUC;',
        'SEX -> EDUC;',
        'RACE -> EDUC;',
        'AGE -> EDUC;',
        'CITIZEN -> EDUC',
        'EDUC -> INCTOT;',
        # R
        'WORKLY -> INCTOT;',
        'CLASSWKR -> INCTOT;',
        'EDUC -> CLASSWKR;',
        'EDUC -> WORKLY;',
        'AGE -> WORKLY'
        'MARST -> WORKLY;',
        'MARST -> CLASSWKR;',

        'CITIZEN -> WORKLY;',
        'AGE -> CLASSWKR;',
        'CITIZEN-> CLASSWKR;',
        'SEX -> WORKLY;',
        'SEX -> CLASSWKR;',
        'RACE -> WORKLY;',
        'RACE -> CLASSWKR;'
    ]

    df = pd.read_csv(PATH + '/2011_2019_D.csv', encoding='utf8').sample(frac=0.1)
    ordinal_atts = {}
    targetClass = 'INCTOT'
    groupingAtt = 'CLASSWKR'
    # #
    fds = ['CLASSWKR']
    CPE.CPE(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
            print_times=True)

def a(row, mod):
    val = row['G']
    return val % mod

def b(row, k):
    val = random.randint(1, k)
    return val

def synthatic(k,tau):
    data = [i for i in range(1, 101)]

    # Create a pandas DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=["G"])
    df['A1'] = df.apply(lambda row: a(row,2), axis=1)
    df['A2'] = df.apply(lambda row: a(row,3), axis=1)
    df['A3'] = df.apply(lambda row: a(row, 5), axis=1)
    df['A4'] = df.apply(lambda row: a(row, 7), axis=1)
    df['T1'] = df.apply(lambda row: b(row, 5), axis=1)
    df['T2'] = df.apply(lambda row: b(row, 5), axis=1)
    df['T3'] = df.apply(lambda row: b(row, 5), axis=1)
    df['O'] = df['T1'] + df['T2'] - df['T3']

    # Display the DataFrame
    print(df)
    actionable_atts = ['T1','T2','T3']
    DAG = [
        'O;',
        'T1;',
        'T2;',
        'T3;',

        'T1 -> O;',
        'T2 -> O;',
        'T3 -> O;'
    ]


    ordinal_atts = {}
    targetClass = 'O'
    groupingAtt = 'G'
    # #
    fds = ['A1','A2','A3','A4']
    CPE.CPE(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
            print_times=True)

    CPE.BF(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
            print_times=True)

if __name__ == '__main__':
    k = 5
    tau = 0.75

    #so(k,tau)
    # german(k,tau)
    #adult(k,tau)
    #accidents(k,tau)
    #impus(k,tau)
    synthatic(5,1)
