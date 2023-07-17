import warnings
warnings.filterwarnings('ignore')
PATH = "./data/"
import CauSumX
import pandas as pd


def so(k, tau):
   actionable_atts = [
      'Gender', 'SexualOrientation', 'EducationParents', 'RaceEthnicity',
      'Age', 'Hobby', 'Student',
   'FormalEducation', 'UndergradMajor', 'DevType', 'HoursComputer',
   'Exercise'
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
   CauSumX.cauSumX(df, DAG, ordinal_atts, targetClass, groupingAtt, fds, k, tau, actionable_atts, True, True,
           print_times=True)

def main():
   k = 3
   tau = 1
   so(k,tau)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
