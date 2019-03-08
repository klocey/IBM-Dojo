from __future__ import division
import numpy as np
from numpy.random import binomial
from random import choice, uniform, randint
import sys
import os
# Part 1 (above): Import modules

mydir = os.path.expanduser('~/GitHub/IBM-Dojo/') # use os to open a path in the same directory to GitHub then IBM-Dojo
sys.path.append(mydir)

###### Model Description ##############

'''
An individual-based model to simulate birth and death among species...
'''

# Part 2 (below): define functions

def modelcolor(imm):
    clr = str()
    if imm <= 1: clr = 'darkred'
    elif imm < 2: clr = 'red'
    elif imm < 3: clr = 'orange'
    elif imm < 4: clr = 'yellow'
    elif imm < 5: clr = 'lawngreen'
    elif imm < 6: clr = 'green'
    elif imm < 7: clr = 'deepskyblue'
    elif imm < 8: clr = 'blue'
    elif imm < 9: clr = 'blueviolet'
    else: clr = 'purple'
    return clr

'''
model color is determine by immmigration rate if immigration is equal to 1 then
the color well be darkred.
'''

def randcolor():
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)

    clr = '#%02x%02x%02x' % (c1, c2, c3)
    return clr

'''

'''

def reproduce(inds, sick, x_coords, y_coords): #Made a function an called it reproduce assigned it the list of inds, sick, x_coords, y_coords

  i1 = list(inds) 
  s1 = list(sick) 
  x1 = list(x_coords) 
  y1 = list(y_coords) 

  '''
  44) list of inds and asignned it the variable of i1
  45) list of sick and asignned it the variable of i1
  46) list of x_coords and asignned it the variable of i1
  47) list of y_coords and asignned it the variable of i1
  we assigned the list new variable because we do not want them to point at the same data
  '''

  for i, val in enumerate(sick):# loop through val of sick
    x = choice([0, 1])
    if x == 1: 
        s1.append(val) 
        max1 = max(inds) + 1 
        i1.append(max1) 
        x1.append(x_coords[i])
        y1.append(y_coords[i])

  '''
  58) randomly choice a number between 0 and 1
  59) if x equal one
  60) list of sick is gonna be extend by val list
  61)  max1 is a unique ID; get the max number of inds and assign it to max1
  62) extend i1 by max1 which has assigned value of max(inds)

  '''

  return i1, s1, x1, y1 

  '''we return i1, s1, x1 and y1  as we dont want the came data from the other list
     they would both point at the same object
  '''

def death(inds, sick, x_coords, y_coords, inf_ded, nat_ded):
# made a function called death and assigned the list of inds, sick, x_coords and y_coords

  i1 = list(inds) 
  s1 = list(sick) 
  x1 = list(x_coords) 
  y1 = list(y_coords) 

  '''
  83) list of inds and assigne it the variable of i1
  84) list of sick and assigned it the variable of s1
  85) list of x_coords and assign it the variable of x1
  86) list of y_coords and assin it the variable of y1

  '''

  for i, val in enumerate(sick):
    x = binomial(1, val*inf_ded)
    if x == 1: 
        i1.pop(0)
        s1.pop(0)
        x1.pop(0)
        y1.pop(0)
  return i1, s1, x1, y1
  '''
  98) randomly choice 1 or 0
  99) if x is choosen then
  100) in list of i1 take out index (0)
  101) in list of s1 take out index (0)
  104) we return i1, s1, x1 and y1 as we dont want the came data from the other list
       they would both point at the same object
  '''

def infection(inds, sick, x_coords, y_coords, inf):

  i1 = randint(0,len(inds)-1)
  i2 = randint(0,len(inds)-1)
  
  x1 = x_coords[i1]
  x2 = x_coords[i2]
  y1 = y_coords[i1]
  y2 = y_coords[i2]
  
  for i, val in enumerate(sick):
    dist = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    pad = 1/(1+dist)
    pof = inf * pad
    x = np.random.binomial(1, pof)
    if x == 1:
      sick[i] = 1
  return inds, sick, x_coords, y_coords


def recover(inds, sick, x_coords, y_coords, rec):
  for i, val in enumerate(sick):
      x = binomial(1, rec)
      if x == 1:
          sick[i] = 0
  return inds, sick, x_coords, y_coords


def dispersal(inds, sick, x_coords, y_coords):
  for num in range(len(sick)): 
    i = randint(0, len(inds)-1) 
    x_coords[i] += uniform(-1, 1) 
    y_coords[i] += uniform(-1, 1) 
  return inds, sick, x_coords, y_coords

  '''
  117) for the range of sick use length for a loop
  118) randomly choose a number between 0 and the length of inds
  119) x_coords[i] += uniform(-1, 1) # += is a shortcut for x = x + y
  120) y_coords[i] += uniform(-1, 1) # += is a shortcut for y = x + y
  '''

def immigration(inds, sick, x_coords, y_coords, S, imm):
  for i in range(imm): # number of orgrainism immirgerating per gen
    z = 0.1 # probability that an immigrant is sick
    s = binomial(1, z)
    
    inds.append(max(inds)+1)
    sick.append(s)
    x_coords.append(uniform(min(x_coords), max(x_coords)))
    y_coords.append(uniform(min(y_coords), max(y_coords)))

  return inds, sick, x_coords, y_coords


# Part 3(below): declare objects/variables

'''
159) get the range from 11 (0, 1, 2, ..., 10). 11 is not included take the range
     then turn that in that into a list. Assign the variable of ms
'''

# part 4 (below) open and clear data files
# txt = comma separated values
OUT = open(mydir + 'CEMs/SimData/inds_data.txt', 'w+') 
OUT.close()                                       

'''
156) open mydir open SimData open inds_data.cvs, Write
     and create a file named inds_data.txt
157) always closed the file that was just open

'''

OUT = open(mydir + 'CEMs/SimData/sick_data.txt', 'w+') 
OUT.close()                                       

'''
166) open mydir open SimData open sick_data.cvs, Write
     and create a file named sick_data.txt
167) always closed the file that was just open
'''

OUT = open(mydir + 'CEMs/SimData/x_coords_data.txt', 'w+')
OUT.close()                                       

'''
175) open mydir open SimData open x_coords_data.cvs, Write and create a file named
     x_coords_data.txt
176) always closed the file that was just open

'''

OUT = open(mydir + 'CEMs/SimData/y_coords_data.txt', 'w+')
OUT.close()

'''
185) open mydir open SimData open y_coords_data.cvs, Write and create a file named 
     y_coords_data.txt
186) always closed the file that was just open
'''

OUT = open(mydir + 'CEMs/SimData/Compiled_Data.txt', 'w+')
OUT.write("model,clr,imm,inf_ded,nat_ded, inf,rec,t,N,Sick,Healthy,area,extinct\n")
OUT.close()

'''
194) open mydir open SimData open Complied_Data.cvs, Write and create a file named 
     y_coords_data.txt
195) 
196) always closed the file that was just open
'''

# Part 5 (Below): run model
for x in range(1):
  N = 1000 #individual organisms
  S = 1  # Number of species
  
  # Primary model parameters  
  ms = list(range(11))
  imm = 5 #choice(ms) # immigration rate
  nat_ded = 0.1
  inf_ded = nat_ded+0.1 #uniform(0, 1) # mortality rate
  
  inf = 0.5 #uniform(0, 1) # infection rate at distance = 0
  rec = 0.5 #uniform(0, 1) # recovery rate
  
  clr = modelcolor(imm)
  inds = list(range(N))
  
  sick = np.random.randint(0, S, N).tolist() 
  x_coords = [0]*N 
  y_coords = [0]*N 

  '''
  206) range of 0 to 999 does not include 1000
  210) inds is a list from 0 to 999, where values are individual IDs
  212) have x_coords list be for 0 to the lsit of individual
  213) have y_coords list be for 0 to the list of individual
  '''

  t = 0 # start at generation 0
  while len(inds) > 0:
    print(len(inds))

    t += 1 # increment generation
    j = choice([0, 1, 2, 3, 4, 5])
    if j == 0:
      inds, sick, x_coords, y_coords = reproduce(inds, sick, x_coords, y_coords)
    # take reprodution list values and assign them to inds, sick, x_coords, y_coords
    elif j == 1:
      inds, sick, x_coords, y_coords = death(inds, sick,x_coords, y_coords, inf_ded, nat_ded)
    # take death list values and assign them to inds, sick, x_coords, y_coords
    elif j == 2:
      inds, sick, x_coords, y_coords = dispersal(inds, sick, x_coords, y_coords)
    elif j == 3:
      inds, sick, x_coords, y_coords = immigration(inds, sick, x_coords, y_coords, S, imm)
    elif j == 4:
      inds, sick, x_coords, y_coords = infection(inds, sick, x_coords, y_coords, inf)
    elif j == 5:
      inds, sick, x_coords, y_coords = recover(inds, sick, x_coords, y_coords, rec)

    Ni = len(inds)
    Si = len(list(set(sick)))
    NumSick = sum(sick)
    Healthy = len(sick) - sum(sick)
    
    if len(x_coords) == 0: A = 0
    else: A = (max(x_coords) - min(x_coords)) * (max(y_coords) - min(y_coords))
      # A = area = length * height

    # take dispersal list values and assign them to inds, sick, x_coords, y_coords
    len_list = [len(inds), len(sick), len(x_coords), len(y_coords)]
    # get the length of inds, sick, x_coords and y_coords then assign the value to
    # the variable of len_list

    # write data to file every so number of time steps
    if t%25 == 0 or Ni == 0:
    # if 25 equal to 0 while running the the program 1000 time then gather data
      OUT = open(mydir + 'CEMs/SimData/inds_data.txt', 'a+')
      outlist = str(inds).strip('[]') # in the list of inds strip all "[]" from the list then assigen it to the variable of outlist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      OUT.write(outlist+'\n')
      #print>>OUT, outlist
      OUT.close()


      OUT = open(mydir + 'CEMs/SimData/sick_data.txt', 'a+')
      outlist = str(sick).strip('[]') # in the list of sick strip all "[]" from the list then assigen it to the variable of oulist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      OUT.write(outlist+'\n')
      #print>>OUT, outlist
      OUT.close()


      OUT = open(mydir + 'CEMs/SimData/x_coords_data.txt', 'a+')
      outlist = str(x_coords).strip('[]') # in the list of x_coords strip all "[]" from the list then assigen it to the variable of outlist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      OUT.write(outlist+'\n')
      #print>>OUT, outlist
      OUT.close()

      OUT = open(mydir + 'CEMs/SimData/y_coords_data.txt', 'a+')
      outlist = str(y_coords).strip('[]') # in the list of y_coords strip all "[]" from the list then assigen it to the variable of oulist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      OUT.write(outlist+'\n')
      #print>>OUT, outlist
      OUT.close()

      OUT = open(mydir + 'CEMs/SimData/Compiled_Data.txt', 'a+')
      extinct = False
      if len(inds) == 0: extinct = True # This True/False designation will be used for accessing data when making figures
      outlist = str([x, clr, imm, inf_ded, nat_ded, inf, rec, t, Ni, NumSick, Healthy, A, extinct]).strip('[]') # in the list of y_coords strip all "[]" from the list then assigen it to the variable of oulist
      '''         model,clr, imm, inf_ded, nat_ded, inf, rec, t, N, Sick, Healthy, area, extinct
      '''
      outlist = outlist.replace(' ', '') # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      outlist = outlist.replace("'", '')
      OUT.write(outlist+'\n')
      #print>>OUT, outlist
      OUT.close()
