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

 
  
# Part 3 (below): declare objects/variables

N = 1000 # Number of individual organisms
S = 100  # Number of species

inds = range(N) # inds is a list from 0 to 999, where values are individual IDs
spes = np.random.randint(0, S, N).tolist()





#print(spes)
#sys.exit()


t = 1000 # Numbers of time steps

