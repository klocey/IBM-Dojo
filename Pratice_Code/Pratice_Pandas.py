import pandas as pd
import sys
import os

mydir = os.path.expanduser('~/GitHub/IBM-Dojo')
df = pd.read_csv(mydir + '/Pratice_Code/Pratice_Pandas_Sheets.txt', delimiter = '\t')

################################### Chapters Houses ############################
Chapters = df.sort_values('Chapter Name')

Chapter_inds = len(Chapters['inds'])
Chapter_males = len(Chapters.loc[(Chapters['Sex'] < 1)])
Chapter_females = len(Chapters.loc[(Chapters['Sex'] == 1)])

Chapter_sick = Chapters.loc[(Chapters['Healthy']) < 1]
Chapters_sick_males = Chapters.loc[(Chapters['Healthy'] < 1) & (Chapters['Sex'] < 1)]
Chapters_sick_females = Chapters.loc[(Chapters['Healthy'] < 1) & (Chapters['Sex'] == 1)]

Chapter_age = Chapters['age']
print(Chapter_age)

#################################### Blue Gap ##################################
Blue_Gap = df.loc[df['Chapter Name'] == 'Blue Gap']

Blue_Gap_inds = len(Blue_Gap['inds'])
Blue_Gap_males =len(Blue_Gap.loc[(Blue_Gap['Sex'] < 1)])
Blue_Gap_females = len(Blue_Gap.loc[(Blue_Gap['Sex'] == 1)])

sick_inds = Blue_Gap.loc[(Blue_Gap['Healthy']) < 1]
sick_males = Blue_Gap.loc[(Blue_Gap['Healthy'] < 1) & (Blue_Gap['Sex'] < 1)]
sick_females = Blue_Gap.loc[(Blue_Gap['Healthy'] < 1) & (Blue_Gap['Sex'] == 1)]

Blue_Gap_age = Blue_Gap['age']
print(Blue_Gap_age)
'''
Blue_Gap_age_0_9 = Blue_Gap.loc[Blue_Gap['age'] > 10]
Blue_Gap_age_10_19 = (len(Blue_Gap.loc[Blue_Gap['age'] > 20]) - int(len(Blue_Gap_age_0_9)))
Blue_Gap_age_20_29 = (len(Blue_Gap.loc[Blue_Gap['age'] > 30]) - int(len(Blue_Gap_age_10_19)))
Blue_Gap_age_30_39 = (len(Blue_Gap.loc[Blue_Gap['age'] > 40]) - int(len(Blue_Gap_age_20_29)))
Blue_Gap_age_40_49 = (len(Blue_Gap.loc[Blue_Gap['age'] > 50]) - int(len(Blue_Gap_age_30_39)))
Blue_Gap_age_50_59 = (len(Blue_Gap.loc[Blue_Gap['age'] > 60]) - int(len(Blue_Gap_age_40_49)))
Blue_Gap_age_60_69 = (len(Blue_Gap.loc[Blue_Gap['age'] > 70]) - int(len(Blue_Gap_age_50_59)))
Blue_Gap_age_70_79 = (len(Blue_Gap.loc[Blue_Gap['age'] > 80]) - int(len(Blue_Gap_age_60_69)))
Blue_Gap_age_80 = (len(Blue_Gap.loc[Blue_Gap['age'] > 90]) - int(len(Blue_Gap_age_70_79)))
'''
#################################### Chinle ###################################
Chinle = df.loc[df['Chapter Name'] == 'Chinle']

#################################### Tsaile ###################################
Tsaile = df.loc[df['Chapter Name'] == 'Tsaile']
