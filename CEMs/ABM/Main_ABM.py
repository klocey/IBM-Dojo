from __future__ import division
import numpy as np
from random import choice
import sys
import os
import pandas as pd


mydir = os.path.expanduser('~/GitHub/IBM-Dojo/CEMs/ABM')
sys.path.append(mydir)

import SimFxns

###### Model Description ##############

OUT = open(mydir + '/SimData/main_data.txt', 'w+')
# Print column headers
print(OUT, 'sim,disease,day,N,Nmale,Nfemale,N_age10orless,N_age20orless, ...') # etc.
#print>>OUT, 'sim,disease,day,N,Nmale,Nfemale,N_age10orless,N_age20orless, ...'
OUT.close()


file_name = '2019_10_01_1330_MasterData-Sheet1.txt'
MainDF = pd.read_csv(mydir + '/GIS_Data_Frame/'+file_name, delimiter="\t")


# Get chapters and chapter population size
# 1. use pandas to pull in master dataframe
# 2. use pandas to get a list of chapter names
# 4. using list of chapter names, get chapter population sizes
# 5. check whether the sum of chapter population sizes adds up to N.
# 6. if sum != N, use the actual sum from above.
# 7. construct list of probabilities.

chapter_names = []
chapter_rel_popsize = [] # relative pop size = probability



num_sims = 1
for sim in range(num_sims):

  N = 173667 # This should be the size of the Navajo Nation
  nat_ded = 0.1
  inf_ded = 0.6
  imm = 2  
  disease = "HantaViruS"
  
  # Generate iDict:
  iDict = {}
  for i in range(N):
      

      # sexes for individuals on the Navajo Nation
      sexes = choice(['m','f'])
      # probabilities for a randomly chosen individual being M or F
      sex_ps = [0.47, 0.53]
      
      sex = np.random.choice(sexes, size=1, replace=True, p=sex_ps)
      
      
      # get age groups (e.g., <10, < 20, etc.) using age demographics of 
      # the Navajo Nation
      age_groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
      # demographies: a list of probabilities that a randomly chosen individual
      # will belong to a given age group. These probabilities must add up to 1.0
      # if all probabilities equal 0.1, then all age groups are equally likely.
      demographies = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
      age = np.random.choice(age_groups, size=1, replace=True, p=demographies)
      
      
      # choose home town (or chapter) according to n/N, where n is the 
      # population size of various towns (or chapters) and N is the population
      # size of the Navajo Nation
    
      home_chapter = np.random.choice(chapter_names, size=1, replace=True, 
                                      p=chapter_rel_popsize)
      
      inf = 0 # all individuals start healthy
      
      iDict[i] = {'sex': sex, 'age': age, 'dsi': 0, 'dsr':0, 'dsv':0, 
               'ebs':0, 'ebr':0, 'ebv':0, 'vac':0, 'rec':0, 'con':0, 
               'infected':inf, 'home_chapter': home_chapter}
      
      
      ''' ADD ADDITIONAL INFORMATION AS NECESSARY
          Need:
              current latitude, current longtidue, etc.
      '''
      
      
  # Iterate over some number of days
  for day in range(365*1): # 365*x = years
      
    for i in len(iDict):
        
        print('simulation:', sim, '| Day:', day, ' | N:', len(inds))

        j = choice([0, 1, 2, 3, 4, 5, 6])
        if j == 0:
            iDict = SimFxns.reproduce(iDict, MainDF, disease)
        elif j == 1:
            iDict = SimFxns.death(iDict, MainDF, disease)
        elif j == 2:
            iDict = SimFxns.dispersal(iDict, MainDF, disease)
        elif j == 3:
            iDict = SimFxns.immigration(iDict, MainDF, disease)
        elif j == 4:
            iDict = SimFxns.infection(iDict, MainDF, disease)
        elif j == 5:
            iDict = SimFxns.recover(iDict, MainDF, disease)
        elif j == 6:
            iDict = SimFxns.Incubation(iDict, MainDF, disease)

    Ni = len(iDict)
    NumSick = 0
    
    for key, value in iDict.items():
        if value['infected'] == 1:
            NumSick += 1


    outlist = [sim, disease, day, N] # list to hold data 
    
    TotalHealthy = Ni - NumSick
    outlist.append(TotalHealthy) # add new info to outlist
    

    ''' The following lines should contain code that will gather data from
    iDict, MainDF, etc.
    
    Population demographics:
        You can do this the hard way (below) or a more creative way.
    '''
####################### Convert Dictionary to dataframe ########################
    NN = pd.DataFrame.from_dict(iDict)
    NN = NN.transpose()
    
    CH = NN.sort_values('home_chapter') # CH is abvr for Chapter house

    CH_inds = len(list(CH))   
    
    CH_males = len(CH.loc[(CH['sex'] < 1)])
    CH_females = len(CH.loc[(CH['sex'] == 1)])
    
    CH_sick = CH.loc[(CH['infecetd']) < 1]
    CH_sick_males = CH.loc[(CH['infected'] < 1) & (CH['Sex'] < 1)]
    CH_sick_females = CH.loc[(CH['infected'] < 1) & (CH['Sex'] == 1)]
        
    CH_age_0_9 = CH.loc[ CH['age'] < 10]
    CH_age_10_19 = len(CH.loc[ CH['age'] < 20])
    CH_age_20_29 = len(CH.loc[ CH['age'] < 30])
    CH_age_30_39 = len(CH.loc[ CH['age'] < 40])
    CH_age_40_49 = len(CH.loc[ CH['age'] < 50])
    CH_age_50_59 = len(CH.loc[ CH['age'] < 60])
    CH_age_60_69 = len(CH.loc[ CH['age'] < 70])
    CH_age_70_79 = len(CH.loc[ CH['age'] < 80])
    CH_age_80 = len(CH.loc[ CH['age'] < 80])

    S_CH_age_0_9 = CH.loc[(CH['age'] < 10) & (CH['infected'] < 1)]
    S_CH_age_10_19 = CH.loc[(CH['age'] < 20) & (CH['infected'] < 1)]
    S_CH_age_20_29 = CH.loc[(CH['age'] < 30) & (CH['infected'] < 1)]
    S_CH_age_30_39 = CH.loc[(CH['age'] < 40) & (CH['infected'] < 1)]
    S_CH_age_40_49 = CH.loc[(CH['age'] < 50) & (CH['infected'] < 1)]
    S_CH_age_50_59 = CH.loc[(CH['age'] < 60) & (CH['infected'] < 1)]
    S_CH_age_60_69 = CH.loc[(CH['age'] < 70) & (CH['infected'] < 1)]
    S_CH_age_70_79 = CH.loc[(CH['age'] < 80) & (CH['infected'] < 1)]
    S_CH_age_80 = CH.loc[(CH['age'] < 80)  & (CH['infected'] < 1)]
        
    # Loop through chapter names:
    for ch in chapter_names:
        
        
        
        '''
        Nc = # Number of individuals in a particular chapter
        Number of males in Tsaile
        Number of females in Tsaile
        Number of persons under age 10 in Tsaile
        Number of persons under age 20 in Tsaile
        Number of persons under age ... in Tsaile
        Number of sick individuals in Tsaile
        Number of sick males in Tsaile
        Number of sick females in Tsaile
        Number of sick persons under age 10 in Tsaile
        Number of sick persons under age 20 in Tsaile
        Number of sick persons under age ... in Tsaile
        '''
    
    # write data to file for every day
    OUT = open(mydir + '/SimData/main_data.txt', 'a+')
    print>>OUT, # what to print
    OUT.close()