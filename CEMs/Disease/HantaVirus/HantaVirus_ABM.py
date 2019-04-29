from __future__ import division
import numpy as np
from random import choice
import sys
import os
# Part 1 (above): Import modules

mydir = os.path.expanduser('~/GitHub/IBM-Dojo/CEMs/Disease/HantaVirus') # use os to open a path in the same directory to GitHub then IBM-Dojo
sys.path.append(mydir)

import ABM_Function as ABM

###### Model Description ##############

'''
An Agent-Based Model to simulate the spread of disease...
'''

# Part 3(below): declare objects/variables

# part 4 (below) open and clear data files
# txt = comma separated values
OUT = open(mydir + 'CEMs/SimData/inds_data.txt', 'w+') 
OUT.close()                                       

OUT = open(mydir + 'CEMs/SimData/sick_data.txt', 'w+') 
OUT.close()                                       

OUT = open(mydir + 'CEMs/SimData/x_coords_data.txt', 'w+')
OUT.close()                                       

OUT = open(mydir + 'CEMs/SimData/y_coords_data.txt', 'w+')
OUT.close()

OUT = open(mydir + 'CEMs/SimData/Compiled_Data.txt', 'w+')
OUT.write("model,clr,imm,inf_ded,nat_ded, inf,rec,t,N,Sick,Healthy,area,extinct\n")
OUT.close()

# Part 5 (Below): run model
for x in range(1):
  N = 1000 #individual organisms
  S = 1  # Number of species
  nat_ded = 0.1
  inf_ded = 0.6
  imm = 2  
  # Primary model parameters 

  clr = ABM(imm)

  # Lists for properties of individuals
  inds = list(range(N))
  sick = [0]*N
  x_coords = [0]*N 
  y_coords = [0]*N 
  ages = np.random.randint(0, 7500, len(inds)) # age in days
  sex = np.random.binomial(1, 0.5, len(inds)) # 1 = male; 0 = female
  dsi = [0]*N
  dsr = [0]*N
  ebs = [0]*N
  ebr = [0]*N
  vac = [0]*N
  rec = [0]*N
  con = [0]*N

  t = 0 # start at generation 0
  while len(inds) > 0:
    print(len(inds))

    t += 1 # increment generation
    j = choice([0, 1, 2, 3, 4, 5, 6])
    if j == 0:
      inds, sick, x_coords, y_coords = ABM.reproduce(inds, sick, x_coords, y_coords)
    # take reprodution list values and assign them to inds, sick, x_coords, y_coords
    elif j == 1:
      inds, sick, x_coords, y_coords = ABM.death(inds, sick,x_coords, y_coords, inf_ded, nat_ded)
    # take death list values and assign them to inds, sick, x_coords, y_coords
    elif j == 2:
      inds, sick, x_coords, y_coords = ABM.dispersa(inds, sick, x_coords, y_coords)
    elif j == 3:
      inds, sick, x_coords, y_coords = ABM.immigration(inds, sick, x_coords, y_coords, S, imm)
    elif j == 4:
      inds, sick, x_coords, y_coords = ABM.infection(inds, sick, x_coords, y_coords)
    elif j == 5:
      inds, sick, x_coords, y_coords = ABM.recover(inds, sick, x_coords, y_coords, rec)
    elif j == 6:
      inds, sick, x_coords, y_coords, dsi = ABM.Incubation(inds, sick, x_coords, y_coords, dsi)

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
      outlist = str([x, clr, imm, inf_ded, nat_ded, rec, t, Ni, NumSick, Healthy, A, extinct, dsi, dsr, vac, ages, sex, ebs, ebr]).strip('[]') # in the list of y_coords strip all "[]" from the list then assigen it to the variable of oulist
      '''         model,clr, imm, inf_ded, nat_ded, rec, t, N, Sick, Healthy, area, extinct
s      '''
      outlist = outlist.replace(' ', '') # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      outlist = outlist.replace("'", '')
      OUT.write(outlist+'\n')
      #print>>OUT, outlist
      OUT.close()
