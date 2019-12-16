from __future__ import division
import numpy as np
from numpy.random import binomial
from random import choice, uniform, randint
from math import radians, cos, sin, asin, sqrt, pi, exp
import scipy

#def agg_data(i, iDict):

import Main_ABM as ABM

def haversine(key, iDict, MainDF):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lat1 = iDict['c_lat']
    lon1 = iDict['c_lon']
    lat2 = iDict['c_lat']
    lon2 = iDict['c_lon']
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km

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


d_list = ["HantaVirus", 'Influenza', 'Ebola']
disease = choice(d_list)

if disease == "HantaVirus":
  inf = 0.5 #uniform(0, 1) # infection rate at distance = 0
elif disease == 'Influenza':
    inf = 0.1
elif disease == 'Ebola':
    inf = 0.8
    
def time_convertor(key, iDict):
    year = iDict['age'] / 365
    
    return iDict, year
        
def update_times(key, iDict, MainDF, disease):
    
    ages = np.array(iDict['ages'])
    ages = ages + 1
    ages = ages.tolist()

    for i, val in enumerate(iDict['vac']): 
        iDict['dsv'] != 90
        if val == 1:
            iDict['dsv'] += 1 
        elif iDict['dsv'] == 90:
            iDict['vac'] = 0

    for i, val in enumerate(iDict['inf']):
        if val == 1:
            iDict['dsi'][i] += 1
        elif val == 0:
            if iDict['ebr'][i] == 1:
                iDict['dsr'][i] += 1

    return iDict

def reproduce(key, iDict, MainDF, disease):
    '''
    Made a function an called it reproduce assigned it the dictionary of iDict, and 
    the GIS Master Dataframe
    '''
    if iDict['sex'] == 'f': # Check if the individual is male or female
        # declare binomial parameters (n, p):
        n = 40 # N is the maxnium age an individual can reproduce
        p = 0.5 #  %0 precent chance the individual will reproduce
        # declare age variable
        age = 20 # The average age an individual will reproduce.efrff
        # below: python code representing the pmf equation of the binomial distribution
        # scipy.special.binom() is the binomial coefficient
        prob_of_repro = scipy.special.binom(n, age) * p**age * (1-p)**(n-age)
     
        # inds, sick, x_coords, y_coords, ages, sex
        i1 = iDict[key]
        x1 = iDict['c_lon'][key]
        y1 = iDict['c_lat'][key]
    
        x = prob_of_repro
        if x == 1:
          
          new_name = max(list(iDict)) + 1
          iDict[new_name] = {'sex': choice('m','f'), 'age': 0, 'dsi': 0, 'dsr':0, 'dsv':0,
               'ebs':0, 'ebr':0, 'ebv':0, 'vac':0, 'rec':0, 'con':0, 
               'inf': 0, 'home_chapter': i1['home_chpater'] ,'c_lat': x1, 
               'c_lon': y1, 'alive': 1}
          
          '''
          iDict[new_name] will add a new individual into the NN population.
          the sex of the new individual should be 50/50, age will be zero 
          as it was just born and home_chapter have to be the same as the 
          parent individaul.

          Sex is the gender of individual, dsi = days since infection, dsr = days since
          recovery, dsv = days since vac, ebs = ever been sick, ebr = ever been recovered,
          vac = vacinated, rec = recovered, con = con, inf = infected, c_lat = current 
          lat, c_lon = current lon. 
         '''
    return iDict

def death(key, iDict, MainDF, disease):
  prob_of_death = 1 - (78.6/(78.6 + iDict['age'])) # 78.6 is the life expect of human
  
  for i, val in enumerate(iDict['inf']):
    x = int()
    if val == 1: x = binomial(1, ABM.inf_ded)
    elif val == 0: x = binomial(1, prob_of_death) 
    if x == 1: 
        iDict['alive'] = 0
    if disease == "HantaVirus":
        Mortality = np.random.uniform(14,21)
        p = (1 - np.random.uniform(0.33,0.5))/Mortality
        x = np.random.binomial(p,1)
        if x == 1:
            iDict['alive'] == 0
  return iDict

def infection(key, iDict, MainDF, disease):
  # inds, sick, x_coords, y_coords, vac, dsi, dsr
  i1 = randint(0,len(iDict)-1)
  i2 = randint(0,len(iDict)-1)
  
  x1 = iDict['c_lat']
  x2 = iDict['c_lon'][i2]
  y1 = iDict['c_lon'][i1]
  y2 = iDict['c_lat'][i2]
  
  for i, val in enumerate(iDict['inf']):
    D = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    pad = 1/(1+D)
    pof = inf * pad
        
    if disease == "HantaVirus": 
        x = np.random.binomial(1, pof)
        if x == 1:
          iDict['inf'][i] = 1

  return iDict

def recover(key, iDict, MainDF, disease):
    # inds, sick, x_coords, y_coords, rec, vac, dsi, ebs, ebr
    p = 1/(np.sqrt(2*pi)*exp(-0.5*((iDict['dsi'] - 17.5))*2))

    for i, val in enumerate(iDict.key('inf')):
        x = binomial(1, np.all(iDict['rec']))
        if x == 1:
            iDict['inf'][i] = 0
    if disease == "HantaVirus":
      rec = np.random.uniform(14,21)
      p = (1 - np.random.uniform(0.33,0.5))/rec
      x = np.random.binomial(p,1)
      if x == 1:
          iDict['inf'] = 0      
    return iDict

def incubation(key, iDict, MainDF, disease):
    # inds, sick, x_coords, y_coords, ages, sex
    for i, val in enumerate(iDict.key('inf')):
        x = np.random.binomial(1,inf)
        if x == 1:   
            iDict['inf'][i] == 1
    if disease == "HantaVirus":
        incubation = np.random.uniform(7,39)
        p = (1 - np.random.uniform(0.33,0.5))/incubation
        x = np.random.binomial(p,1)
        if x == 1:
            iDict['inf'] == 1
    return iDict
 
def dispersal(key, iDict, MainDF, disease):
  
  # inds, sick, x_coords, y_coords
  for num in range(len(iDict)): 
    i = randint(0, len(iDict.key)-1) 
    iDict['c_lat'][i] += uniform(-1, 1) 
    iDict['c_lon'] += uniform(-1, 1) 
  return iDict

def immigration(key, iDict, MainDF, disease):
  imm = list(range(11))
  m = choice(imm)
  # inds, sick, x_coords, y_coords, S, imm
  for i in range(m): # number of orgrainism immirgerating per gen
    z = 0.1 # probability that an immigrant is sick
    s = binomial(1, z)
    
    iDict.append(max(iDict['inds'])+1)
    iDict['inf'].append(s)
    iDict['c_lat'].append(uniform(min(iDict['c_lat']), max(iDict['c_lat'])))
    iDict['c_lon'].append(uniform(min(iDict['c_lon']), max(iDict['c_lon'])))
  
  return iDict