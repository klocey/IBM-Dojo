from __future__ import division
import numpy as np
from random import choice
import sys
import os
import pandas as pd

mydir = os.path.expanduser('~/GitHub/IBM-Dojo/CEMs/ABM')
sys.path.append(mydir)

#import SimFxns

#OUT = open(mydir + '/SimData/main_data.txt', 'w+')
#print(OUT, 'sim,disease,day,N,Nmale,Nfemale,N_age10orless,N_age20orless, ...') # etc.
#OUT.close()
file_name = '2019_10_28_1345_MasterData.tsv'
MainDF = pd.read_csv(mydir + '/GIS_Data_Frame/'+file_name, delimiter="\t")

chapter_names = list(set(MainDF['Chapter']))
#print len(chapter_names)
#sys.exit()

chapter_rel_popsize = [] # relative pop size = probability

num_sims = 1
for sim in range(num_sims):
    
  N = 1736 # This should be the size of the Navajo Nation
  nat_ded = 0.1
  inf_ded = 0.6
  imm = 2  
  disease = "HantaViruS"
  
  # Generate iDict:
  iDict = {}
  for i in range(N):
       
      # sexes for individuals on the Navajo Nation
      sexes = ['m','f']
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
      
      rel_N = [(N/109)/N]*109
      #print sum(rel_N)
      #print sys.exit()
      home_chapter = np.random.choice(chapter_names, size=1, replace=True, p=rel_N)[0]
      
      inf = 0 # all individuals start healthy
      
      c_lat = MainDF['Lat']# latitude of the home chaper
      c_lon = MainDF['Lon']# similar to above
      
      iDict[i] = {'sex': sex, 'age': age, 'dsi': 0, 'dsr':0, 'dsv':0, 
               'ebs':0, 'ebr':0, 'ebv':0, 'vac':0, 'rec':0, 'con':0, 
               'inf': inf, 'home_chapter': home_chapter, 'c_lat': c_lat, 
               'c_lon': c_lon, 'alive': 1}
      
      # IN THIS DICTIONARY (iDict):
      #   0 = NO, 1 = YES for 'rec', 'inf', 'vac', and 'alive'

      
      ''' ADD ADDITIONAL INFORMATION AS NECESSARY
          Need:
              current latitude, current longtidue, etc.
      '''
      
  # Iterate over some number of days
  for day in range(365*1): # 365*x = years
      
    agg_data = {}
    for ch in chapter_names:
      # agg_data can include as much chapter specific info as needed
      agg_data[ch] = {
              # Note: ls = []*100 represents a list of 100 elements, where
              # each element is an age corresponding to its index.
              # So: ls[0] would hold the value for the number of individuals of age 0.
              
              'm_a_inf_age': [0]*101, 'm_a_rec_age': [0]*101, 'm_a_vac_age': [0]*101,
              'm_d_inf_age': [0]*101, 'm_d_rec_age': [0]*101, 'm_d_vac_age': [0]*101, 
              'f_a_inf_age': [0]*101, 'f_a_rec_age': [0]*101, 'f_a_vac_age': [0]*101,
              'f_d_inf_age': [0]*101, 'f_d_rec_age': [0]*101, 'f_d_vac_age': [0]*101}
              

    #print agg_data[chapter_names[0]]
    #sys.exit()                 
    
    Ni = len(iDict)
    print('simulation:', sim, '| Day:', day, ' | N:', Ni)
    for key, val in iDict.items():
        
        print(key)
        #sys.exit()

        # SimFxns ARE COMMENTED OUT FOR THE PURPOSE OF JUST HAVING THE CODE RUN
        # AND HAVING agg_data INITIATED AND PROCESSED
        
        '''
        j = choice([0, 1, 2, 3, 4, 5, 6])
        if j == 0:
            iDict = SimFxns.reproduce(key, iDict, MainDF, disease)
        elif j == 1:
            iDict = SimFxns.death(key, iDict, MainDF, disease)
        elif j == 2:
            iDict = SimFxns.dispersal(key, iDict, MainDF, disease)
        elif j == 3:
            iDict = SimFxns.immigration(key, iDict, MainDF, disease)
        elif j == 4:
            iDict = SimFxns.infection(key, iDict, MainDF, disease)
        elif j == 5:
            iDict = SimFxns.recover(key, iDict, MainDF, disease)
        elif j == 6:
            iDict = SimFxns.incubation(key, iDict, MainDF, disease)
        '''

        inf = val['inf']
        rec = val['rec']
        vac = val['vac']
        age = val['age']
        sex = val['sex']
        alive = val['alive']
        ch = val['home_chapter']
        
        p1, p2, p3 = str(), str(), str()
        
        if sex == 'm': p1 = 'm_'
        else: p1 = 'f_'
        
        if alive == 1: p2 = 'a_'
        else: p2 = 'd_'
        
        if rec == 0:
            p3 = 'rec_'
            agg_data[ch][p1+p2+p3+'age'][age] += 1
        if inf == 0:
            p3 = 'inf_'
            agg_data[ch][p1+p2+p3+'age'][age] += 1
        if vac == 0:
            p3 = 'inf_'
            agg_data[ch][p1+p2+p3+'age'][age] += 1



        
    print(agg_data['Becenti'])
    sys.exit()
        
    outlist = [sim, disease, day, N] # list to hold data 
    
    # Process data in agg_data to get data for outlist
        
    
    
    # write data to file for every day
    #OUT = open(mydir + '/SimData/main_data.txt', 'a+')
    #print>>OUT, # what to print
    #OUT.close()