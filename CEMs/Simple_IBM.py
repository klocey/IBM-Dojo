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
  53) list of inds and asignned it the variable of i1
  54) list of sick and asignned it the variable of i1
  55) list of x_coords and asignned it the variable of i1
  56) list of y_coords and asignned it the variable of i1
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
  67) randomly choice a number between 0 and 1
  68) if x equal one
  69) list of sick is gonna be extend by val list
  70)  max1 is a unique ID; get the max number of inds and assign it to max1
  71) extend i1 by max1 which has assigned value of max(inds)

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

  for i, val in enumerate(sick):
    x = int()
    if val == 1: x = binomial(1, inf_ded)
    elif val == 0: x = binomial(1, nat_ded)
    if x == 1: 
        i1.pop(0)
        s1.pop(0)
        x1.pop(0)
        y1.pop(0)
    if disease == "HantaVirus":
        Mortality = np.random.uniform(14,21)
        p = (1 - np.random.uniform(0.33,0.5))/Mortality
        x = np.random.binomial(p,1)
        if x == 1:
            i1.pop(0)
            s1.pop(0)
            x1.pop(0)
            y1.pop(0)
  return i1, s1, x1, y1

'''
  92) list of inds and assigne it the variable of i1
  93) list of sick and assigned it the variable of s1
  94) list of x_coords and assign it the variable of x1
  95) list of y_coords and assin it the variable of y
  100) randomly choice 1 or 0
  101) if x is choosen then
  102) in list of i1 take out index (0)
  103) in list of s1 take out index (0)
  106) if the disease is HantaVirus then follow these parameters
  107) The disease life span will be between 14 and 21 days 
  108) The possible of dying from HantaVirus ranging from 33% to 50% than with
       disease life span we will divide it to get mortality rate for the individuals
  109) at random choose a 1 or the variable of p and assign it to x
  115) we return i1, s1, x1 and y1 as we dont want the came data from the other list
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
    D = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    pad = 1/(1+D)
    if disease == 'Influenza':
        pof = inf * pad
    else:
        pof = float(inf)
    r = 4
    R = 2*r
    print(R)
        
    if disease == "HantaVirus": 
        x = np.random.binomial(1, pof)
        if x == 1:
          sick[i] = 1
    
    elif disease == "Influenza":
        x = np.random.binomial(1, pof)
        if x == 1:
          sick[i] = 1
    
    elif disease == "Ebola":
        x = np.random.binomial(1, pof)
        if x == 1:
          sick[i] = 1
  return inds, sick, x_coords, y_coords

'''
137) randomly choose an individuals from the inds list and assign it the variable 
     i1
138) randomly choose an individuals from the inds list and assign it the variable 
     i2
140) get the x coordinates for i1 from the x_coords list and assign the value to
     variable x1
141) get the x coordinates for i2 from the x_coords list and assign the value to
     variable x2
142) get the y coordinates for i1 from the y_coords list and assign the value to
     variable y1
143) get the y coordinates for i2 from the y_coords list and assign the value to
     variable y2 
146) Use the Pythagorean Theorem to get the distance betwwen i1 and i2 then assign 
     that value to the variable of D meaning distance
147) 1/(1+D) is to get the probably of getting infected affected by distance with
     the value we assign it the variable of pad which means "Probably Affected by 
     Distance" 
149) use the value that was assigned to variable "inf" multipy it by the value that
     was assigned to pad. Assign that value to variable "pof" which means "Probably 
     Of Infection" It well be a number between 0 and 1 but never going above 1 or below 0 
152) 4 is the radius of every individuals.
153) multiply 2 by the variable r than assign the value to the variable R
'''


def recover(inds, sick, x_coords, y_coords, rec):
  for i, val in enumerate(sick):
      x = binomial(1, rec)
      if x == 1:
          sick[i] = 0
  if disease == "HantaVirus":
    rec = np.random.uniform(14,21)
    p = (1 - np.random.uniform(0.33,0.5))/rec
    x = np.random.binomial(p,1)
    if x == 1:
        sick = 0      
  return inds, sick, x_coords, y_coords
'''
200) randomly choose a 1 or 0, it affected by the rec list 
201) if x equal 1 then get the sick individuals and cure it from the disease
204) randomly choose a number between 14 and 21. This is how long HantaVirus last
205) randomly choice a number betweem 0.33 to 0.5 that use the variable "rec" to 
     to get the probably of recovering from HantaVirus 
'''

def Incubation(inds, sick, x_coords, y_coords, inf):
    for i, val in enumerate(sick):
        x = np.random.binomial(1,inf)
        if x == 1:
            sick[i] = 0
    if disease == "HantaVirus":
        incubation = np.random.uniform(7,39)
        p = (1 - np.random.uniform(0.33,0.5))/incubation
        x = np.random.binomial(p,1)
    return inds, sick, x_coords, y_coords, inf

def dispersal(inds, sick, x_coords, y_coords):
  for num in range(len(sick)): 
    i = randint(0, len(inds)-1) 
    x_coords[i] += uniform(-1, 1) 
    y_coords[i] += uniform(-1, 1) 
  return inds, sick, x_coords, y_coords

  '''
  ) for the range of sick use length for a loop
  168) randomly choose a number between 0 and the length of inds
  169) x_coords[i] += uniform(-1, 1) # += is a shortcut for x = x + y
  170) y_coords[i] += uniform(-1, 1) # += is a shortcut for y = x + y
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
181) get the range from 11 (0, 1, 2, ..., 10). 11 is not included take the range
     then turn that in that into a list. Assign the variable of ms
'''

# part 4 (below) open and clear data files
# txt = comma separated values
OUT = open(mydir + 'CEMs/SimData/inds_data.txt', 'w+') 
OUT.close()                                       

'''
202) open mydir open SimData open inds_data.cvs, Write
     and create a file named inds_data.txt
203) always closed the file that was just open

'''

OUT = open(mydir + 'CEMs/SimData/sick_data.txt', 'w+') 
OUT.close()                                       

'''
212) open mydir open SimData open sick_data.cvs, Write
     and create a file named sick_data.txt
213) always closed the file that was just open
'''

OUT = open(mydir + 'CEMs/SimData/x_coords_data.txt', 'w+')
OUT.close()                                       

'''
221) open mydir open SimData open x_coords_data.cvs, Write and create a file named
     x_coords_data.txt
222) always closed the file that was just open

'''

OUT = open(mydir + 'CEMs/SimData/y_coords_data.txt', 'w+')
OUT.close()

'''
231) open mydir open SimData open y_coords_data.cvs, Write and create a file named 
     y_coords_data.txt
232) always closed the file that was just open
'''

OUT = open(mydir + 'CEMs/SimData/Compiled_Data.txt', 'w+')
OUT.write("model,clr,imm,inf_ded,nat_ded, inf,rec,t,N,Sick,Healthy,area,extinct\n")
OUT.close()

'''
240) open mydir open SimData open Complied_Data.cvs, Write and create a file named 
     y_coords_data.txt
241) 
241) always closed the file that was just open
'''

# Part 5 (Below): run model
for x in range(1):
  N = 1000 #individual organisms
  S = 1  # Number of species
  nat_ded = 0.1
  imm = 2  
  # Primary model parameters 
  d_list = ["HantaVirus", "Influenza", "Ebola"]
  disease = choice(d_list);
  
  if disease == "HantaVirus":
    #https://www.rightdiagnosis.com/c/cold/stats.htm
    ''' The common cold. An Adenovirus that rarely ever causes death but often 
    infects a large portion of a population. '''
    
    inf_ded = nat_ded+0.5 #uniform(0, 1) # mortality rate    
    inf = 0.5 #uniform(0, 1) # infection rate at distance = 0
    rec = 0.6 #uniform(0, 1) # recovery rate
    
  elif disease == "Influenza":
    inf_ded = nat_ded+0.1 #uniform(0, 1) # mortality rate    
    inf = 0.8 #uniform(0, 1) # infection rate at distance = 0
    rec = 0.3 #uniform(0, 1) # recovery rate
  
  elif disease == "Ebola":    
    inf_ded = nat_ded+0.7 #uniform(0, 1) # mortality rate https://thehill.com/policy/healthcare/220644-ebola-death-rate-rises-to-70-percent    
    inf = 0.6 #uniform(0, 1) # infection rate at distance = 0
    rec = 0.3 #uniform(0, 1) # recovery rate 
  
  print(disease)

  clr = modelcolor(imm)

  # Lists for properties of individuals
  inds = list(range(N))
  sick = np.random.randint(0, S, N).tolist() 
  x_coords = [0]*N 
  y_coords = [0]*N 
  ages = np.random.randint(0, 7500, len(inds)) # age in days
  sex = np.random.binomial(1, 0.5, len(inds)) # 1 = male; 0 = female

  '''
  253) range of 0 to 999 does not include 1000
  210) inds is a list from 0 to 999, where values are individual IDs
  286) have x_oords list be for 0 to the lsit of individual
  287) have y_coords list be for 0 to the list of individual
  '''

  t = 0 # start at generation 0
  while len(inds) > 0:
    print(len(inds))

    t += 1 # increment generation
    j = choice([0, 1, 2, 3, 4, 5, 6])
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
    elif j == 6:
      inds, sick, x_coords, y_coords = Incubation(inds, sick, x_coords, y_coords, inf)

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
    if t%1 == 0 or Ni == 0:
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
