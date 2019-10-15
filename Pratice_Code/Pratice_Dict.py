from __future__ import division
import numpy as np
from random import choice
from numpy.random import binomial
from random import randint

'''
List = []
Function = ()
Dictionarys = {}

'''


age =randint(0,100) # Age is randomly choosen from 0 to 100
sex = np.random.binomial(1, 0.5) # Gender is 1 or 0 they have 50% chance of happening
clat = randint(0,1000) # Lat range from 0 to 1000
clon = randint(0,1000) # Lon range from 0 to 1000
healthy = np.random.binomial(1, 0.3) # Healthy is ethier 1 or 0 and they have a 30% chance of being healthy 
iDict = {}

for i in range(5):
    iDict[i] = {age, sex, clat,
         clon, healthy}
'''
print(iDict.keys())
print(list(iDict.keys())[0])
'''

#'''
keylist = [iDict]
rkey = choice(keylist)
rani = rkey

print(keylist)
#'''