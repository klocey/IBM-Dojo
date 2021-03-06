import pandas as pd
import sys
import os
from random import choice
import numpy as np
from timeit import default_timer as timer

mydir = os.path.expanduser('~/GitHub/Python-ABMs')
df = pd.read_csv(mydir + '/Pratice_Code/Pratice_Pandas_Sheets.txt', delimiter = '\t')
######################################## Dict #################################
chapter_names = ['BG']
chapter_rel_popsize = [1.0] # relative pop size = probability

################################### Chapters Houses ############################
#print(df.shape) # 20 rows x 10 columns
Chapters = df.sort_values('Chapter Name') # inappropriate name
#print(Chapters.shape) # 20 rows x 10 columns


Chapter_inds = len(Chapters['inds']) # Going to be 20, inappropriate name

Chapter_males = len(Chapters.loc[(Chapters['Sex'] < 1)]) # inappropriate name
#print(Chapter_males)
Chapter_females = len(Chapters.loc[(Chapters['Sex'] == 1)]) # inappropriate name
#print(Chapter_females)


Chapter_sick = Chapters.loc[(Chapters['Healthy']) < 1] # inappropriate name
#print(Chapter_sick.shape)


Chapters_sick_males = Chapters.loc[(Chapters['Healthy'] < 1) & (Chapters['Sex'] < 1)]
Chapters_sick_females = Chapters.loc[(Chapters['Healthy'] < 1) & (Chapters['Sex'] == 1)]

num_sims = 1
cols = ['sex', 'age', 'dsi', 'dsr', 'dsv', 'ebs', 'ebr', 'ebv', 'vac',
          'rec', 'con', 'infected', 'home_ch']

#iDF = pd.DataFrame(columns = cols)


for sim in range(num_sims):

  N = 1736 # This should be the size of the Navajo Nation 173667
  nat_ded = 0.1
  inf_ded = 0.6
  imm = 2  
  disease = "HantaViruS"
  
  # Generate iDict:
  iDict = {}
  for i in range(N):
      

      # sexes for individuals on the Navajo Nation
      sexes = ['m', 'f']
      # probabilities for a randomly chosen individual being M or F
      sex_ps = [0.47, 0.53]
      
      sex = np.random.choice(sexes, size=1, replace=True, p=sex_ps)[0]
      
      
      # get age groups (e.g., <10, < 20, etc.) using age demographics of 
      # the Navajo Nation
      age_groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
      # demographies: a list of probabilities that a randomly chosen individual
      # will belong to a given age group. These probabilities must add up to 1.0
      # if all probabilities equal 0.1, then all age groups are equally likely.
      demographies = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
      age = np.random.choice(age_groups, size=1, replace=True, p=demographies)[0]
      
      
      # choose home town (or chapter) according to n/N, where n is the 
      # population size of various towns (or chapters) and N is the population
      # size of the Navajo Nation
    
      home_chapter = np.random.choice(chapter_names, size=1, replace=True, 
                                      p=chapter_rel_popsize)[0]
      
      inf = 0 # all individuals start healthy
      
      iDict[i] = {'sex': sex, 'age': age, 'dsi': 0, 'dsr':0, 'dsv':0, 
               'ebs':0, 'ebr':0, 'ebv':0, 'vac':0, 'rec':0, 'con':0, 
               'infected':inf, 'home_chapter': home_chapter}
      
      
      #ind = {'sex': sex, 'age': age, 'dsi': 0, 'dsr':0, 'dsv':0, 
      #         'ebs':0, 'ebr':0, 'ebv':0, 'vac':0, 'rec':0, 'con':0, 
      #         'infected':inf, 'home_ch': home_chapter}
      
      #iDF = iDF.append(ind, ignore_index=True)


################################# Convert iDict ################################

<<<<<<< HEAD
#NN = pd.DataFrame.from_dict(iDict)
#NN = NN.transpose()


start = timer()

df = pd.DataFrame(columns=['sex', 'age', 'dsi', 'dsr', 'dsv', 
               'ebs', 'ebr', 'ebv', 'vac', 'rec', 'con', 
               'infected', 'home_chapter'])
    
=======
NN = pd.DataFrame(iDict)
#NN = pd.DataFrame.from_dict(iDict)
NN = NN.transpose()


>>>>>>> 8ac91b6fa2bc4983851c6bf244d4216f5098f2c7
end = timer()

print NN.iloc[0]
print(end - start) # Time in seconds

<<<<<<< HEAD
=======



>>>>>>> 8ac91b6fa2bc4983851c6bf244d4216f5098f2c7
################################# Chapters Houses ##############################
'''
NN = NN.sort_values('home_chapter') # CH is abvr for Chapter house

NN_inds = len(list(NN))   
   
NN_males = len(NN.loc[(NN['sex'] == 'm')])
NN_females = len(NN.loc[(NN['sex'] == 'f')])
    
NN_sick = NN.loc[(NN['infected']) < 1]
NN_sick_males = NN.loc[(NN['infected'] < 1) & (NN['sex'] == 'm')]
NN_sick_females = NN.loc[(NN['infected'] < 1) & (NN['sex'] == 'f')]
        
NN_age_0_9 = NN.loc[NN['age'] < 10]
NN_age_10_19 = NN.loc[NN['age'] < 20]
NN_age_20_29 = NN.loc[NN['age'] < 30]
NN_age_30_39 = NN.loc[NN['age'] < 40]
NN_age_40_49 = NN.loc[NN['age'] < 50]
NN_age_50_59 = NN.loc[NN['age'] < 60]
NN_age_60_69 = NN.loc[NN['age'] < 70]
NN_age_70_79 = NN.loc[NN['age'] < 80]
NN_age_80 = NN.loc[NN['age'] < 80]
 
S_NN_age_0_9 = NN.loc[(NN['age'] < 10) & (NN['infected'] < 1)]
S_NN_age_10_19 = NN.loc[(NN['age'] < 20) & (NN['infected'] < 1)]
S_NN_age_20_29 = NN.loc[(NN['age'] < 30) & (NN['infected'] < 1)]
S_NN_age_30_39 = NN.loc[(NN['age'] < 40) & (NN['infected'] < 1)]
S_NN_age_40_49 = NN.loc[(NN['age'] < 50) & (NN['infected'] < 1)]
S_NN_age_50_59 = NN.loc[(NN['age'] < 60) & (NN['infected'] < 1)]
S_NN_age_60_69 = NN.loc[(NN['age'] < 70) & (NN['infected'] < 1)]
S_NN_age_70_79 = NN.loc[(NN['age'] < 80) & (NN['infected'] < 1)]
S_NN_age_80 = NN.loc[(NN['age'] < 80)  & (NN['infected'] < 1)]
Chapter_age = NN['age']  

for ch in range(N):
    Home = list(NN.groupby(['home_chapter']))
    age = NN.groupby(['age'])
    sex = list(NN['home_chapter'].groupby(NN['sex']))
    inf = NN.groupby(['infected'])
    print(age)
    '''
#################################### Blue Gap ##################################
<<<<<<< HEAD
'''
=======
<<<<<<< HEAD
BG = df.loc[df['Chapter Name'] == 'Blue Gap']

BG_inds = len(BG['inds'])
BG_males =len(BG.loc[(BG['Sex'] < 1)])
BG_females = len(BG.loc[(BG['Sex'] == 1)])

sick_inds = BG.loc[(BG['Healthy']) < 1]
sick_males = BG.loc[(BG['Healthy'] < 1) & (BG['Sex'] < 1)]
sick_females = BG.loc[(BG['Healthy'] < 1) & (BG['Sex'] == 1)]

BG_age = BG['age']
print(BG_age)


# Iterate over rows using iterrows
for i, row in BG.iterrows():
    if row['age'] < 10:
        BG_0_9 += 1
    elif row['age'] < 20:
        BG_10_19 += 1
    elif row['age'] < 30:
        BG_20_29 += 1
    elif row['age'] < 40:
        BG_30_39 += 1
    elif row['age'] < 50:
        BG_40_49 += 1
    elif row['age'] < 60:
        BG_50_59 += 1
    elif row['age'] < 70:
        BG_60_69 += 1
    elif row['age'] < 80:
        BG_70_79 += 1
    
        
# use shorter names!!
BG_age_0_9 = BG.loc[BG['age'] > 10]
BG_age_10_19 = (len(BG.loc[BG['age'] > 20]) - int(len(BG_age_0_9)))
BG_age_20_29 = (len(BG.loc[BG['age'] > 30]) - int(len(BG_age_10_19)))
BG_age_30_39 = (len(BG.loc[BG['age'] > 40]) - int(len(BG_age_20_29)))
BG_age_40_49 = (len(BG.loc[BG['age'] > 50]) - int(len(BG_age_30_39)))
BG_age_50_59 = (len(BG.loc[BG['age'] > 60]) - int(len(BG_age_40_49)))
BG_age_60_69 = (len(BG.loc[BG['age'] > 70]) - int(len(BG_age_50_59)))
BG_age_70_79 = (len(BG.loc[BG['age'] > 80]) - int(len(BG_age_60_69)))
BG_age_80 = (len(BG.loc[BG['age'] > 90]) - int(len(BG_age_70_79)))

=======
>>>>>>> 8ac91b6fa2bc4983851c6bf244d4216f5098f2c7
CH = df.loc[df['Chapter Name'] == 'Blue Gap']

CH_inds = len(BG['inds'])
BG_males =len(BG.loc[(BG['Sex'] < 1)])
BG_females = len(BG.loc[(BG['Sex'] == 1)])

sick_inds = BG.loc[(BG['Healthy']) == 1]
sick_males = BG.loc[(BG['Healthy'] == 1) & (BG['Sex'] < 1)]
sick_females = BG.loc[(BG['Healthy'] == 1) & (BG['Sex'] == 1)]
  
BG_age = BG['age']
# print(BG_age)
BG_age_0_9 = BG.loc[BG['age'] < 10]
BG_age_10_19 = len(BG.loc[BG['age'] < 20])
BG_age_20_29 = len(BG.loc[BG['age'] < 30])
BG_age_30_39 = len(BG.loc[BG['age'] < 40])
BG_age_40_49 = len(BG.loc[BG['age'] < 50])
BG_age_50_59 = len(BG.loc[BG['age'] < 60])
BG_age_60_69 = len(BG.loc[BG['age'] < 70])
BG_age_70_79 = len(BG.loc[BG['age'] < 80])
BG_age_80 = len(BG.loc[BG['age'] < 90])

S_BG_0_9 = BG.loc[(BG['age'] < 10) & (BG['Healthy'] < 1)]
S_BG_10_19 = BG.loc[(BG['age'] < 20) & (BG['Healthy'] < 1)]
S_BG_20_29 = BG.loc[(BG['age'] < 30) & (BG['Healthy'] < 1)]
S_BG_30_39 = BG.loc[(BG['age'] < 40) & (BG['Healthy'] < 1)]
S_BG_40_49 = BG.loc[(BG['age'] < 50) & (BG['Healthy'] < 1)]
S_BG_50_59 = BG.loc[(BG['age'] < 60) & (BG['Healthy'] < 1)]
S_BG_60_69 = BG.loc[(BG['age'] < 70) & (BG['Healthy'] < 1)]
S_BG_70_79 = BG.loc[(BG['age'] < 80) & (BG['Healthy'] < 1)]
S_BG_age_80 = BG.loc[(BG['age'] < 90) & (BG['Healthy'] < 1)]
print(BG)
print('\n\n')
print(S_BG_40_49)
'''

'''
print(BG_age_0_9)
print(BG_age_10_19)
print(BG_age_20_29)
print(BG_age_30_39)
print(BG_age_40_49)
print(BG_age_50_59)
'''

#################################### Chinle ###################################
#Chinle = df.loc[df['Chapter Name'] == 'Chinle']

#################################### Tsaile ###################################
#Tsaile = df.loc[df['Chapter Name'] == 'Tsaile']
