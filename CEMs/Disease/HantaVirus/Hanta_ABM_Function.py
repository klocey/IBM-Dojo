from __future__ import division
import numpy as np
from numpy.random import binomial
from random import choice, uniform, randint

# Part 2 (below): define functions

d_list = ["HantaVirus"]
disease = choice(d_list); 
if disease == "HantaVirus":
  inf = 0.5 #uniform(0, 1) # infection rate at distance = 0

  
def update_times(ages, dsr, dsi, dsv, sick, ebs, ebr,vac, rec):
    ages = np.array(ages)
    ages = ages + 1
    ages = ages.tolist()
    
    
    
    for i, val in enumerate(vac): 
        dsv != 90
        if val == 1:
            dsv[i] += 1 
        elif dsv == 90:
            vac[i] = 0

    for i, val in enumerate(sick):
        if val == 1:
            dsi[i] += 1
        elif val == 0:
            if ebr[i] == 1:
                dsr[i] += 1

    return ages, dsr, dsi, dsv, ebs, ebr, vac, rec


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

def randcolor():
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)

    clr = '#%02x%02x%02x' % (c1, c2, c3)
    return clr

def reproduce(inds, sick, x_coords, y_coords, ages, sex): #Made a function an called it reproduce assigned it the list of inds, sick, x_coords, y_coords

  i1 = list(inds) 
  s1 = list(sick) 
  x1 = list(x_coords) 
  y1 = list(y_coords) 

  for i, val in enumerate(sick):# loop through val of sick
    x = choice([0, 1])
    if x == 1: 
        s1.append(val) 
        max1 = max(inds) + 1 
        i1.append(max1) 
        x1.append(x_coords[i])
        y1.append(y_coords[i])

  return i1, s1, x1, y1 

def death(inds, sick, x_coords, y_coords, inf_ded, nat_ded, ages, sex, dsi):
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


def infection(inds, sick, x_coords, y_coords, vac, dsi, dsr):

  i1 = randint(0,len(inds)-1)
  i2 = randint(0,len(inds)-1)
  
  x1 = x_coords[i1]
  x2 = x_coords[i2]
  y1 = y_coords[i1]
  y2 = y_coords[i2]
  
  for i, val in enumerate(sick):
    D = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    pad = 1/(1+D)
    pof = inf * pad
        
    if disease == "HantaVirus": 
        x = np.random.binomial(1, pof)
        if x == 1:
          sick[i] = 1
  return inds, sick, x_coords, y_coords

def recover(inds, sick, x_coords, y_coords, rec, vac, dsi, ebs, ebr):
  for i, val in enumerate(sick):
      x = binomial(1, np.all(rec))
      if x == 1:
          sick[i] = 0
  if disease == "HantaVirus":
    rec = np.random.uniform(14,21)
    p = (1 - np.random.uniform(0.33,0.5))/rec
    x = np.random.binomial(p,1)
    if x == 1:
        sick = 0      
  return inds, sick, x_coords, y_coords


def Incubation(inds, sick, x_coords, y_coords, ages, sex):
    for i, val in enumerate(sick):
        x = np.random.binomial(1,inf)
        if x == 1:
            sick[i] = 0
    if disease == "HantaVirus":
        incubation = np.random.uniform(7,39)
        p = (1 - np.random.uniform(0.33,0.5))/incubation
        x = np.random.binomial(p,1)
    return inds, sick, x_coords, y_coords

def dispersal(inds, sick, x_coords, y_coords):
  for num in range(len(sick)): 
    i = randint(0, len(inds)-1) 
    x_coords[i] += uniform(-1, 1) 
    y_coords[i] += uniform(-1, 1) 
  return inds, sick, x_coords, y_coords

def immigration(inds, sick, x_coords, y_coords, S, imm):
  for i in range(imm): # number of orgrainism immirgerating per gen
    z = 0.1 # probability that an immigrant is sick
    s = binomial(1, z)
    
    inds.append(max(inds)+1)
    sick.append(s)
    x_coords.append(uniform(min(x_coords), max(x_coords)))
    y_coords.append(uniform(min(y_coords), max(y_coords)))
  return inds, sick, x_coords, y_coords


N = 1000 #individual organisms
S = 1  # Number of species
nat_ded = 0.1
inf_ded = 0.6
imm = 2  
# Primary model parameters 

clr = (imm)
# Lists for properties of individuals
inds = list(range(N))
sick = [0]*N
x_coords = [0]*N 
y_coords = [0]*N 
ages = np.random.randint(0, 7500, len(inds)) # age in days
sex = np.random.binomial(1, 0.5, len(inds)) # 1 = male; 0 = female
dsi = [0]*N # Days since infection
dsr = [0]*N # Days since recovery
dsv = [0]*N # Days since Vaccinated
ebs = [0]*N # Ever been sick
ebr = [0]*N # Ever been recovered
ebv = [0]*N # Ever been vaccined
vac = [0]*N # Vaccinated
rec = [0]*N # Recovered
con = [0]*N # Contagious