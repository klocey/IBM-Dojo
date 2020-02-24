from __future__ import division
import numpy as np
from random import choice
import sys
import os
import pandas as pd
from numpy.random import seed

mydir = os.path.expanduser('~/GitHub/Python-ABMs/CEMs/ABM')
sys.path.append(mydir)

import SimFxns



file_name = '2020_01_28_2231_MasterData.txt'
MainDF = pd.read_csv(mydir + '/GIS_Data_Frame/'+file_name, delimiter="\t")


ch_names = list(MainDF['Chapters'])
ch_lats = list(MainDF['Lat'])
ch_lons = list(MainDF['Lon'])


#for i, val in enumerate(ch_names):
#    print(val, ch_lats[i], ch_lons[i])
#sys.exit()
    

#print(len(ch_names), len(ch_lats), len(ch_lats))
#sys.exit()

ch_pops = list(MainDF['Population'])
N = sum(ch_pops)


ch_rel_popsize = np.array(ch_pops)/N # relative pop size = probability

############ Above: code taken from Main_ABM.py


# -----------------------------------------------------------------------------


############ Below: declaring dataframe using column names
      
column_names = ['sex', 'age', 'dsi', 'dsr', 'dsv','ebs', 'ebr', 'ebv', 'vac', 
                'rec', 'con', 'inf', 'home_chapter', 'c_lat', 'c_lon', 'alive']
               
               
df_NN = pd.DataFrame(columns = column_names)

#print('Numbers of rows and columns in dataframe:', df_NN.shape)
#print('Row names of dataframe:', list(df_NN))


############ Below: filling dataframe

### Get sexes
df_NN['sex'] = np.random.binomial(1, 0.53, N)  # 1 == Female ; 0 = Male    


### Get ages
age_groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
demographies = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
df_NN['age'] = np.random.choice(age_groups, size=N, replace=True, 
     p=demographies)




### Get home chapters
#rand_seed = np.random.randint(0)

seed(0)
df_NN['home_chapter'] = np.random.choice(ch_names, size = N, 
     replace=True, p=ch_rel_popsize)

seed(0)
df_NN['c_lat'] = np.random.choice(ch_lats, size = N, 
     replace=True, p=ch_rel_popsize)

seed(0)
df_NN['c_lon'] = np.random.choice(ch_lons, size = N, 
     replace=True, p=ch_rel_popsize)



#print(df_NN['home_chapter'][0], df_NN['c_lat'][0], df_NN['c_lon'][0])


df_NN['dsi'] = 0
df_NN['dsr'] = 0
df_NN['dss'] = 0
df_NN['ebs'] = 0
df_NN['ebr'] = 0
df_NN['ebv'] = 0
df_NN['vac'] = 0
df_NN['rec'] = 0
df_NN['con'] = 0
df_NN['inf'] = 0
df_NN['alive'] = 1

print(df_NN.shape)
print(list(df_NN))