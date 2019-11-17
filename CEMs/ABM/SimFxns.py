from __future__ import division
import numpy as np
from numpy.random import binomial
from random import choice, uniform, randint



#def agg_data(i, iDict):
    
    
    


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


d_list = ["HantaVirus"]
disease = choice(d_list); 
if disease == "HantaVirus":
  inf = 0.5 #uniform(0, 1) # infection rate at distance = 0

  
def update_times(iDict, MainDF, disease):
        
    #ages, dsr, dsi, dsv, sick, ebs, ebr,vac, rec
    
    ages = np.array(iDict['ages'])
    ages = ages + 1
    ages = ages.tolist()
    

    for i, val in enumerate(iDict['vac']): 
        iDict['dsv'] != 90
        if val == 1:
            iDict['dsv[i]'] += 1 
        elif iDict['dsv'] == 90:
            iDict['vac[i]'] = 0

    for i, val in enumerate(iDict['sick']):
        if val == 1:
            iDict['dsi'][i] += 1
        elif val == 0:
            if iDict['ebr'][i] == 1:
                iDict['dsr'][i] += 1

    return iDict

def reproduce(iDict, MainDF, disease): #Made a function an called it reproduce assigned it the list of inds, sick, x_coords, y_coords

  # inds, sick, x_coords, y_coords, ages, sex
  i1 = list(iDict['inds']) 
  s1 = list(iDict['sick']) 
  x1 = list(x_coords) 
  y1 = list(y_coords) 

  for i, val in enumerate(iDict['sick']):# loop through val of sick
    x = choice([0, 1])
    if x == 1: 
        s1.append(val) 
        max1 = max(iDict['inds']) + 1 
        i1.append(max1) 
        x1.append(x_coords[i])
        y1.append(y_coords[i])

  return iDict

def death(iDict, MainDF, disease):
  # inds, sick, x_coords, y_coords, inf_ded, nat_ded, ages, sex, dsi
  # made a function called death and assigned the list of inds, sick, x_coords and y_coords

  i1 = list(iDict['inds']) 
  s1 = list(iDict['sick']) 
  x1 = list(x_coords) 
  y1 = list(y_coords) 

  for i, val in enumerate(iDict['sick']):
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
  return iDict

def infection(iDict, MainDF, disease):

  # inds, sick, x_coords, y_coords, vac, dsi, dsr
  i1 = randint(0,len(iDict['inds'])-1)
  i2 = randint(0,len(iDict['inds'])-1)
  
  x1 = x_coords[i1]
  x2 = x_coords[i2]
  y1 = y_coords[i1]
  y2 = y_coords[i2]
  
  for i, val in enumerate(iDict['sick']):
    D = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    pad = 1/(1+D)
    pof = inf * pad
        
    if disease == "HantaVirus": 
        x = np.random.binomial(1, pof)
        if x == 1:
          iDict['sick'][i] = 1

  return iDict

def recover(iDict, MainDF, disease):
    
  # inds, sick, x_coords, y_coords, rec, vac, dsi, ebs, ebr
  for i, val in enumerate(iDict['sick']):
      x = binomial(1, np.all(iDict['rec']))
      if x == 1:
          iDict['sick'][i] = 0
  if disease == "HantaVirus":
    rec = np.random.uniform(14,21)
    p = (1 - np.random.uniform(0.33,0.5))/rec
    x = np.random.binomial(p,1)
    if x == 1:
        iDict['sick'] = 0      
  return iDict

def Incubation(iDict, MainDF, disease):
    # inds, sick, x_coords, y_coords, ages, sex
    for i, val in enumerate(iDict['sick']):
        x = np.random.binomial(1,inf)
        if x == 1:
            iDict['sick'][i] = 0
    if disease == "HantaVirus":
        incubation = np.random.uniform(7,39)
        p = (1 - np.random.uniform(0.33,0.5))/incubation
        x = np.random.binomial(p,1)
    return iDict

def dispersal(iDict, MainDF, disease):
  
  # inds, sick, x_coords, y_coords
  for num in range(len(iDict['sick'])): 
    i = randint(0, len(iDict['inds'])-1) 
    x_coords[i] += uniform(-1, 1) 
    y_coords[i] += uniform(-1, 1) 
  return iDict

def immigration(iDict, MainDF, disease):

  # inds, sick, x_coords, y_coords, S, imm
  for i in range(imm): # number of orgrainism immirgerating per gen
    z = 0.1 # probability that an immigrant is sick
    s = binomial(1, z)
    
    iDict['inds'].append(max(iDict['inds'])+1)
    iDict['sick'].append(s)
    x_coords.append(uniform(min(x_coords), max(x_coords)))
    y_coords.append(uniform(min(y_coords), max(y_coords)))
  
  return iDict