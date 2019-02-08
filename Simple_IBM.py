from __future__ import division
import numpy as np
from random import choice, uniform
import sys

# Part 1 (above): Import modules

###### Model Description ##############

'''
An individual-based model to simulate birth and death among species
'''


# Part 2 (below): define functions

def reproduce(inds, spes):
  
  i1 = list(inds)
  s1 = list(spes)    
    
  for val in spes:
    x = choice([0, 1])
    if x == 1:
        s1.extend([val])
        max1 = max(inds) + 1
        i1.extend([max1])
  return i1, s1


def death(inds, spes):
  
  i1 = list(inds)
  s1 = list(spes)

  for val in spes:
    x = choice([0, 1])
    if x == 1:
        i1.pop(0)
        s1.pop(0)
        print(len(i1),len(s1))
  return i1, s1

# dispersal
'''
four different list 
1. inds
2. spes
3. x_coords
4. y_coords
'''

# Part 3(below): declare objects/variables

N = 1000 # Number of individual organisms
S = 100  # Number of species

inds = list(range(N)) # inds is a list from 0 to 999, where values are individual IDs
spes = np.random.randint(0, S, N).tolist()

# Part 4 (Below): run model

inds, spes = reproduce(inds, spes)
inds, spes = death(inds, spes)