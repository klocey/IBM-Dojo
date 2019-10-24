from __future__ import division
import numpy as np
from numpy.random import binomial
from random import randint

'''
List = []
Function = ()
Dictionarys = {Key: Value}
Dictionaries are date types
'''
################################################################################
n = 5
iDict = {}
print("Idict #1")
      
for i in range(n):
    iDict['age'] = randint(0,100)
    iDict['sex'] = np.random.binomial(1, 0.5)
    iDict['clat'] = randint(-1000,1000)
    iDict['clon'] = randint(-1000,1000)
    iDict['healthy'] = np.random.binomial(1, 0.3)
    print(iDict)
    
################################################################################
N = 2
iDict_2 = {}
print('iDict #2')
      
for i in range(N):
    age_2 = randint(0,100) 
    sex_2 = np.random.binomial(1, 0.5) 
    clat_2 = randint(0,1000) 
    clon_2 = randint(0,1000) 
    healthy_2 = np.random.binomial(1, 0.3) 
    iDict_2[i] = {'age' : age_2, 'Sex' : sex_2, 'clat' : clat_2, 'clon' : clon_2,
         'healthy' : healthy_2}
    print(iDict_2)
    

################################################################################
print("iDict #3")
for i in range(5):
    age_3 = randint(0,100) # Age is randomly choosen from 0 to 100
    sex_3 = np.random.binomial(1, 0.5) # Gender is 1 or 0 they have 50% chance of happening
    clat_3 = randint(0,1000) # Lat range from 0 to 1000
    clon_3 = randint(0,1000) # Lon range from 0 to 1000
    healthy_3 = np.random.binomial(1, 0.3) # Healthy is ethier 1 or 0 and they have a 30% chance of being healthy 
    iDict_3 = {age_3, sex_3, clat_3, clon_3, healthy_3}
    print(iDict_3)

'''
  Random model  
'''
################################################################################
iDict_4 = {'age': 19, 'Gender': "male", 'clat': 10, 'clon': 120, 'Healthy': "No"}
print('iDict #4')
for k, i in iDict_4.items():
    print(k,i)
'''
  When print function is ran we are able to get the key and value from the
  dictionaries 
'''  
###############################################################################
'''
print(iDict.keys())
print(list(iDict.keys())[0])
'''

'''
keylist = [iDict]
rkey = choice(keylist)
rani = rkey

print(keylist)
'''
