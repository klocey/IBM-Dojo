from __future__ import division
import numpy as np
from random import choice, uniform, randint
import sys
import os

# Part 1 (above): Import modules
mydir = os.path.expanduser('~/GitHub/IBM-Dojo/')
sys.path.append(mydir)

###### Model Description ##############

'''
An individual-based model to simulate birth and death among species
'''


# Part 2 (below): define functions

def reproduce(inds, spes, x_coords, y_coords):
  
  i1 = list(inds)
  s1 = list(spes)
  x1 = list(x_coords)
  y1 = list(y_coords)    
    
  for val in spes:
    x = choice([0, 1])
    if x == 1:
        s1.extend([val])
        max1 = max(inds) + 1
        i1.extend([max1])
  return i1, s1, x1, y1


def death(inds, spes, x_coords, y_coords):
  
  i1 = list(inds)
  s1 = list(spes)
  x1 = list(x_coords)
  y1 = list(y_coords)

  for val in spes:
    x = choice([0, 1])
    if x == 1:
        i1.pop(0)
        s1.pop(0)
  return i1, s1, x1, y1


def dispersal(inds, spes, x_coords, y_coords):
  for num in range(len(spes)):
    i = randint(0, len(inds))
    x_coords[i] += uniform(-1, 1)
    y_coords[i] += uniform(-1, 1) 
  return inds, spes, x_coords, y_coords
  
# Part 3(below): declare objects/variables

N = 1000 # Number of individual organisms
S = 100  # Number of species

inds = list(range(N)) # inds is a list from 0 to 999, where values are individual IDs
spes = np.random.randint(0, S, N).tolist()
x_coords = [0]*N
y_coords = [0]*N
    

# Part 4 (Below): run model
OUT = open(mydir + 'SimData/inds_data.csv', 'w+')
OUT.close()

OUT = open(mydir + 'SimData/spes_data.csv', 'w+')
OUT.close()

OUT = open(mydir + 'SimData/x_coords_data.csv', 'w+')
OUT.close()

OUT = open(mydir + 'SimData/y_coords_data.csv', 'w+')
OUT.close()

for x in range(10000):
  inds, spes, x_coords, y_coords = reproduce(inds, spes, x_coords, y_coords)
  inds, spes, x_coords, y_coords = death(inds, spes,x_coords, y_coords)
  inds, spes, x_coords, y_coords = dispersal(inds, spes, x_coords, y_coords)

  len_list = [len(inds), len(spes), len(x_coords), len(y_coords)]
  if min(len_list) != max(len_list):
      print(len_list)
      sys.exit()
      
  # write data to file every 10 time steps
  if x%25 == 0:
      
    OUT = open(mydir + 'SimData/inds_data.csv', 'a+')
    outlist = str(inds).strip('[]')
    outlist = outlist.replace(" ", "")
    OUT.write(outlist)
    OUT.close()

    OUT = open(mydir + 'SimData/spes_data.csv', 'a+')
    outlist = str(spes).strip('[]')
    outlist = outlist.replace(" ", "")
    OUT.write(outlist)
    OUT.close()

    OUT = open(mydir + 'SimData/x_coords_data.csv', 'a+')
    outlist = str(x_coords).strip('[]')
    outlist = outlist.replace(" ", "")
    OUT.write(outlist)
    OUT.close()

    OUT = open(mydir + 'SimData/y_coords_data.csv', 'a+')
    outlist = str(y_coords).strip('[]')
    outlist = outlist.replace(" ", "")
    OUT.write(outlist)
    OUT.close()
