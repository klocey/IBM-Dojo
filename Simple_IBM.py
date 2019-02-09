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
Here are the steps to code up:

1. Declare a function called "dispersal" and pass it inds, spes, x_coords, and y_coords.
2. Declare a 'for' loop and have it iterate a number of times equal to the length of inds. 
3. Inside the for loop: 
  a. Choose a number at random using the 'randint' function. The number should be between 0 and the length of inds list.
  The number will represent an index in the four lists. Assign the number to an object called 'i'. 
  b. Choose from the numbers [-1, 0, 1] at random using the 'choice' function. Assign the number to an object called 'direction'. 
      -1 means move left, 0 means stay put, 1 means move right
  c. add the value of 'direction' to x_coords[i].
  d. Choose from the numbers [-1, 0, 1] at random using the 'choice' function. Assign the number to an object called 'direction'. 
      -1 means move down, 0 means stay put, 1 means move up
  e. add the value of 'direction' to y_coords.
4. Once the loop has completed, return inds, spes, x_coords, and y_coords.

The function results in moving individuals in combinations of up, down, left, right, or no movement at all.
'''


# Part 3(below): declare objects/variables

N = 1000 # Number of individual organisms
S = 100  # Number of species

inds = list(range(N)) # inds is a list from 0 to 999, where values are individual IDs
spes = np.random.randint(0, S, N).tolist()

# Part 4 (Below): run model

inds, spes = reproduce(inds, spes)
inds, spes = death(inds, spes)
