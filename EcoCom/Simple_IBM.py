from __future__ import division
import numpy as np
from random import choice
import sys
import os

import IBM_Function as IBM
# Part 1 (above): Import modules

mydir = os.path.expanduser('~/GitHub/IBM-Dojo/EcoCom') # use os to open a path in the same directory to GitHub then IBM-Dojo
sys.path.append(mydir)

###### Model Description ##############

'''
An individual-based model to simulate birth and death among species...
'''

# Part 3(below): declare objects/variables

N = 1000 #individual organisms
S = 100  # Number of species

areas = []
Ns = []
Ss = []
iS = []
gens = []
ms = list(range(11))

'''
154) we made an empty list then assinged the varibale areas
155) we made an empty list then assinged the varibale Ns
156) we made an empty list then assinged the varibale Ss
157) we made an empty list then assinged the varibale iS
158) we made an empty list then assinged the varibale gens
159) get the range from 11 (0, 1, 2, ..., 10). 11 is not included take the range
     then turn that in that into a list. Assign the variable of ms
'''

# part 4 (below) open and clear data files
# txt = comma separated values
OUT = open(mydir + 'SimData/inds_data.txt', 'w+') 
OUT.close()                                       

'''
156) open mydir open SimData open inds_data.cvs, Write
     and create a file named inds_data.txt
157) always closed the file that was just open

'''

OUT = open(mydir + 'SimData/spes_data.txt', 'w+') 
OUT.close()                                       

'''
166) open mydir open SimData open spes_data.cvs, Write
     and create a file named spes_data.txt
167) always closed the file that was just open
'''

OUT = open(mydir + 'SimData/x_coords_data.txt', 'w+')
OUT.close()                                       

'''
175) open mydir open SimData open x_coords_data.cvs, Write and create a file named
     x_coords_data.txt
176) always closed the file that was just open

'''

OUT = open(mydir + 'SimData/y_coords_data.txt', 'w+')
OUT.close()

'''
185) open mydir open SimData open y_coords_data.cvs, Write and create a file named 
     y_coords_data.txt
186) always closed the file that was just open
'''

OUT = open(mydir + 'SimData/Compiled_Data.txt', 'w+')
OUT.write("model,clr,m,t,N,S,area,extinct\n")
OUT.close()

'''
194) open mydir open SimData open Complied_Data.cvs, Write and create a file named 
     y_coords_data.txt
195) 
196) always closed the file that was just open
'''

# Part 5 (Below): run model
for x in range(1000):
  m = choice(ms)
  clr = IBM.modelcolor(m)
  print(m)
  inds = list(range(N))
  spes = np.random.randint(0, S, N).tolist() 
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
    t += 1 # increment generation
    j = choice([0, 1, 2, 3])
    if j == 0:
      inds, spes, x_coords, y_coords = IBM.reproduce(inds, spes, x_coords, y_coords)
    # take reprodution list values and assign them to inds, spes, x_coords, y_coords
    elif j == 1:
      inds, spes, x_coords, y_coords = IBM.death(inds, spes,x_coords, y_coords)
    # take death list values and assign them to inds, spes, x_coords, y_coords
    elif j == 2:
      inds, spes, x_coords, y_coords = IBM.dispersal(inds, spes, x_coords, y_coords)
    elif j == 3:
      inds, spes, x_coords, y_coords = IBM.immigration(inds, spes, x_coords, y_coords, S, m)

    Ni = len(inds)
    Si = len(list(set(spes)))
    if Ni <= 0:
      gens.append(t)

    Ns.append(Ni)
    Ss.append(Si)

    if len(x_coords) == 0: A = 0
    else: A = (max(x_coords) - min(x_coords)) * (max(y_coords) - min(y_coords))
      # A = area = length * height
    areas.append(A)

    # take dispersal list values and assign them to inds, spes, x_coords, y_coords
    len_list = [len(inds), len(spes), len(x_coords), len(y_coords)]
    # get the length of inds, spes, x_coords and y_coords then assign the value to
    # the variable of len_list

    # write data to file every so number of time steps
    if t%20 == 0 or Ni == 0:
    # if 25 equal to 0 while running the the program 1000 time then gather data
      OUT = open(mydir + 'SimData/inds_data.txt', 'a+')
      outlist = str(inds).strip('[]') # in the list of inds strip all "[]" from the list then assigen it to the variable of outlist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      #OUT.write(outlist)
      print>>OUT, outlist
      OUT.close()


      OUT = open(mydir + 'SimData/spes_data.txt', 'a+')
      outlist = str(spes).strip('[]') # in the list of spes strip all "[]" from the list then assigen it to the variable of oulist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      #OUT.write(outlist)
      print>>OUT, outlist
      OUT.close()


      OUT = open(mydir + 'SimData/x_coords_data.txt', 'a+')
      outlist = str(x_coords).strip('[]') # in the list of x_coords strip all "[]" from the list then assigen it to the variable of outlist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      #OUT.write(outlist)
      print>>OUT, outlist
      OUT.close()

      OUT = open(mydir + 'SimData/y_coords_data.txt', 'a+')
      outlist = str(y_coords).strip('[]') # in the list of y_coords strip all "[]" from the list then assigen it to the variable of oulist
      outlist = outlist.replace(" ", "") # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      #OUT.write(outlist)
      print>>OUT, outlist
      OUT.close()

      OUT = open(mydir + 'SimData/Compiled_Data.txt', 'a+')
      extinct = False
      if len(inds) == 0: extinct = True # This True/False designation will be used for accessing data when making figures
      outlist = str([x, clr, m, t, Ni, Si, A, extinct]).strip('[]') # in the list of y_coords strip all "[]" from the list then assigen it to the variable of oulist
      outlist = outlist.replace(' ', '') # Use the variable of outlist and replace(x, y) all " " with "" then assign the value back to outlist
      outlist = outlist.replace("'", '')
      #OUT.write(outlist)
      print>>OUT, outlist
      OUT.close()
