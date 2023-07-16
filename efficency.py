import pandas as pd
import warnings
warnings.filterwarnings('ignore')
PATH = "C:/Users/brity/OneDrive/Desktop/sudeepa/data/"
import time
THETA = 0.5
import case_study
import itertools
import random

def germanData():
    actionable_atts = ['status', 'duration', 'credit_history',
                       'amount', 'savings', 'employment_duration', 'installment_rate',
                       'personal_status_sex', 'other_debtors', 'present_residence', 'property',
                       'age', 'other_installment_plans', 'housing', 'number_credits', 'job',
                       'people_liable', 'telephone', 'foreign_worker']

    fractions = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    f = open('data.txt','w')
    f.write('tuples\ttime\n')
    # Loop through the fractions and sample the data
    for i in fractions:
        df = pd.read_csv(PATH + 'german_credit_data_new.csv', encoding='utf8').sample(frac=i)
        l = len(df)
        t1, t2, t3, all = case_study.german(i,5, 1, actionable_atts, True, True, print_times=True)
        f.write(str(l)+"\t"+str(all)+"\n")
    f.close()


def germanAtts():


    actionable_atts = ['status', 'duration', 'credit_history',
       'amount', 'savings', 'employment_duration', 'installment_rate',
       'personal_status_sex', 'other_debtors', 'present_residence', 'property',
       'age', 'other_installment_plans', 'housing', 'number_credits', 'job',
       'people_liable', 'telephone', 'foreign_worker']


    for k in range(1,len(actionable_atts)+1):
        atts = random.sample(actionable_atts, k)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(atts)
        print(k)
        t1, t2, t3, all = case_study.german(8, 1, atts, True, True, print_times=True)
        print(t1, t2, t3, all)

def adultAtts():
    actionable_atts = ['age', 'workclass',
                       'education.num', 'marital.status', 'relationship', 'race',
                       'sex', 'hours.per.week',
                       'native.country']

    for k in range(1,9):
        atts = random.sample(actionable_atts, k)
        print("###########################")
        print(atts)
        print(k)
        t1, t2, t3, all = case_study.adult(5, 1, atts, True, True, print_times=True)
        print(t1, t2, t3, all)

def adultData():
    actionable_atts = ['age', 'workclass',
                       'education.num', 'marital.status', 'relationship', 'race',
                       'sex', 'hours.per.week',
                       'native.country']

    fractions = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    f = open('adult_data.txt','w')
    f.write('tuples\ttime\n')
    # Loop through the fractions and sample the data
    for i in fractions:
        df = pd.read_csv(PATH + 'adult_new.csv', encoding='utf8').sample(frac=i)
        l = len(df)
        t1, t2, t3, all = case_study.adult(i,5, 1, actionable_atts, True, True, print_times=True)
        f.write(str(l)+"\t"+str(all)+"\n")
    f.close()

def soData():
    actionable_atts = ['Gender', 'SexualOrientation', 'EducationParents', 'RaceEthnicity',
                       'Dependents', 'Age', 'Hobby', 'Student', 'FormalEducation',
                       'UndergradMajor', 'DevType', 'HoursComputer',
                       'Exercise']

    fractions = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    f = open('so_data.txt','w')
    f.write('tuples\ttime\n')
    # Loop through the fractions and sample the data
    for i in fractions:
        df = pd.read_csv(PATH + 'so_countries_col_new.csv', encoding='utf8').sample(frac=i)
        l = len(df)
        t1, t2, t3, all = case_study.soCountry(i,5, 1, actionable_atts, True, True, print_times=True)
        f.write(str(l)+"\t"+str(all)+"\n")
    f.close()

def adultAttsOPT():
    actionable_atts = ['age', 'workclass',
                       'education.num', 'marital.status', 'relationship', 'race',
                       'sex', 'hours.per.week',
                       'native.country']
    f = open('atts_time', 'w')
    f.write('atts\tt1\tt2\tt3\tall\n')
    for k in range(1,9):
        atts = random.sample(actionable_atts, k)
        print("###########################")
        print(atts)
        print(k)
        t1, t2, t3, all = case_study.adult(5, 1, atts, True, True, print_times=True)
        print(t1, t2, t3, all)
        f.write(str(k) + "+\t" + str(t1) + "\t" + str(t2) + "\t" + str(t3) + "\t" + str(all) + "\n")
    f.close()

def soAtts():
    actionable_atts = ['Gender', 'SexualOrientation', 'EducationParents', 'RaceEthnicity',
       'Dependents', 'Age', 'Hobby','Student', 'FormalEducation',
                       'UndergradMajor', 'DevType','HoursComputer',
        'Exercise']
    f = open('atts_time','w')
    f.write('atts\tt1\tt2\tt3\tall\n')
    for k in range(1,len(actionable_atts)+1):
        atts = random.sample(actionable_atts, k)
        print("###########################")
        print(atts)
        print(k)
        t1, t2, t3, all = case_study.soCountry(8, 1, atts, True, True, print_times=True)
        f.write(str(k)+"+\t"+str(t1)+"\t"+str(t2)+"\t"+str(t3)+"\t"+str(all)+"\n")
    f.close()

def covidAtts():
    actionable_atts = ['Confirmed', 'Recovered', 'Active',
       'NewCases', 'NewDeaths', 'NewRecovered',
       'RecoveredPer100Cases',
       'ConfirmedLastWeek',
       'HDI',
       'LifeExpectancyAtBirth',
       'AvgTemperature']
    f = open('atts_time','w')
    f.write('atts\tt1\tt2\tt3\tall\n')
    for k in range(1,len(actionable_atts)+1):
        atts = random.sample(actionable_atts, k)
        print("###########################")
        print(atts)
        print(k)
        t1, t2, t3, all = case_study.covid(8, 1, atts, True, True, print_times=True)
        f.write(str(k)+"+\t"+str(t1)+"\t"+str(t2)+"\t"+str(t3)+"\t"+str(all)+"\n")
    f.close()





if __name__ == '__main__':
    #adultAtts()
    #germanAtts()
    #soAtts()
    #covidAtts()

    adultData()
    #germanData()
    #soData()


