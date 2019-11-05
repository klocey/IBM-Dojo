import pandas as pd
import sys
import os
from random import choice
import numpy as np

mydir = os.path.expanduser('~/GitHub/IBM-Dojo')
df = pd.read_csv(mydir + '/Pratice_Code/Pratice_Pandas_Sheets.txt', delimiter = '\t')
######################################## Dict #################################
chapter_names = ['BG']
chapter_rel_popsize = [1.0] # relative pop size = probability

num_sims = 1
for sim in range(num_sims):

  N = 17366 # This should be the size of the Navajo Nation
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

################################# Convert iDict ################################
NN = pd.DataFrame.from_dict(iDict)
NN = NN.transpose()
################################# Chapters Houses ##############################
'''
Chapters = NN.sort_values('home_chapter')

Chapter_inds = len(Chapters['inds'])
Chapter_males = len(Chapters.loc[(Chapters['Sex'] < 1)])
Chapter_females = len(Chapters.loc[(Chapters['Sex'] == 1)])

Chapter_sick = Chapters.loc[(Chapters['Healthy']) < 1]
Chapters_sick_males = Chapters.loc[(Chapters['Healthy'] < 1) & (Chapters['Sex'] < 1)]
Chapters_sick_females = Chapters.loc[(Chapters['Healthy'] < 1) & (Chapters['Sex'] == 1)]

Chapter_age = Chapters['age']  
#print(Chapters)

#################################### Blue Gap ##################################
BG = df.loc[df['Chapter Name'] == 'Blue Gap']

BG_inds = len(BG['inds'])
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
