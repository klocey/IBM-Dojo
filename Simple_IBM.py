from __future__ import division
import numpy as np
from random import choice, uniform, randint
import sys
import os
import matplotlib.pyplot as plt

# we import modules 

# Part 1 (above): Import modules
mydir = os.path.expanduser('~/GitHub/IBM-Dojo/') # use os to open a path in the same directory to GitHub then IBM-Dojo
sys.path.append(mydir)

###### Model Description ##############

'''
An individual-based model to simulate birth and death among species
'''

# Part 2 (below): define functions

def reproduce(inds, spes, x_coords, y_coords): #Made a function an called it reproduce assigned it the list of inds, spes, x_coords, y_coords
  
  i1 = list(inds) # list of inds and asignned it the variable of i1 
  s1 = list(spes) # list of spes and asignned it the variable of i1
  x1 = list(x_coords) # list of x_coords and asignned it the variable of i1
  y1 = list(y_coords) # list of y_coords and asignned it the variable of i1   
  # we assigned the list new variable because we do not want them to point at the same data

  for i, val in enumerate(spes):# loop through val of spes                       
    x = choice([0, 1]) # randomly choice a number between 0 and 1
    if x == 1: # if x equal one 
        s1.append(val) # list of spes is gonna be extend by val list
        max1 = max(inds) + 1 # max1 is a unique ID; get the max number of inds and assign it to max1
        i1.append(max1) # extend i1 by max1 which has assigned value of max(inds)
        x1.append(x_coords[i])
        y1.append(y_coords[i])
        
  return i1, s1, x1, y1 # we return i1, s1, x1 and y1  as we dont want the came data from the other list 
                        # they would both point at the same object

def death(inds, spes, x_coords, y_coords):# mdade a function called death and assigned the list of inds, spes, x_coords and y_coords
  
  i1 = list(inds) # list of inds and assigne it the variable of i1
  s1 = list(spes) # list of spes and assigned it the variable of s1
  x1 = list(x_coords) # list of x_coords and assign it the variable of x1
  y1 = list(y_coords) # list of y_coords and assin it the variable of y1

  for val in spes:
    x = choice([0, 1]) # randomly choice 1 or 0 
    if x == 1: # if x is choosen then
        i1.pop(0) # in list of i1 take out index (0)
        s1.pop(0) # in list of s1 take out index (0)
        x1.pop(0)
        y1.pop(0)
  return i1, s1, x1, y1 # we return i1, s1, x1 and y1  as we dont want the came data from the other list 
                        # they would both point at the same object

def dispersal(inds, spes, x_coords, y_coords):
  for num in range(len(spes)): # for the range of spes use length for a loop
    i = randint(0, len(inds)-1) # randomly choose a number between 0 and the length of inds
    x_coords[i] += uniform(-1, 1) # += is a shortcut for x = x + y 
    y_coords[i] += uniform(-1, 1) # += is a shortcut for y = x + y 
  return inds, spes, x_coords, y_coords

def immigration(inds, spes, x_coords, y_coords, S):
  m = 8 #m is the immigration rate
  for i in range(m): # number of orgrainism immirgerating per gen
    s = randint(0, S)
    inds.append(max(inds)+1)
    spes.append(s)
    x_coords.append(uniform(min(x_coords), max(x_coords)))
    y_coords.append(uniform(min(y_coords), max(y_coords)))

  return inds, spes, x_coords, y_coords
  
# Part 3(below): declare objects/variables

N = 1000 #individual organisms
S = 100  # Number of species

areas = []
Ns = []
Ss = []
iS = []
gens = []
ms = range(30)

inds = list(range(N)) # inds is a list from 0 to 999, where values are individual IDs
spes = np.random.randint(0, S, N).tolist() # 
x_coords = [0]*N # have x_coords list be for 0 to the lsit of individual
y_coords = [0]*N # have y_coords list be for 0 to the list of individual

# Part 4 (Below): run model
# csv = comma separated values
OUT = open(mydir + 'SimData/inds_data.csv', 'w+') # open mydir open SimData open inds_data.cvs, Write 
OUT.close()                                       # and create a file named inds_data.csv 
                                                  # always closed the file that was just open

OUT = open(mydir + 'SimData/spes_data.csv', 'w+') # open mydir open SimData open spes_data.cvs, Write 
OUT.close()                                       # and create a file named spes_data.csv 
                                                  # always closed the file that was just open

OUT = open(mydir + 'SimData/x_coords_data.csv', 'w+')# open mydir open SimData open x_coords_data.cvs, Write 
OUT.close()                                       # and create a file named x_coords_data.csv 
                                                  # always closed the file that was just open

OUT = open(mydir + 'SimData/y_coords_data.csv', 'w+') # open mydir open SimData open y_coords_data.cvs, Write 
OUT.close()                                       # and create a file named y_coords_data.csv 
                                                  # always closed the file that was just open
  
  
for m in ms:
  t = 0 # start at generation 0  
  while len(inds) > 0:
    t += 1 # increment generation
    j = choice([0, 1, 2, 3])
    if j == 0:
      inds, spes, x_coords, y_coords = reproduce(inds, spes, x_coords, y_coords)
    # take reprodution list values and assign them to inds, spes, x_coords, y_coords
    elif j == 1: 
      inds, spes, x_coords, y_coords = death(inds, spes,x_coords, y_coords)
    # take death list values and assign them to inds, spes, x_coords, y_coords
    elif j == 2:
      inds, spes, x_coords, y_coords = dispersal(inds, spes, x_coords, y_coords)
    elif j == 3:
      inds, spes, x_coords, y_coords = immigration(inds, spes, x_coords, y_coords, S)

    Ni = len(inds)
    Si = len(list(set(spes)))
    if Ni <= 0: break    
    
    Ns.append(Ni)
    Ss.append(Si)
    gens.append(t)
    A = (max(x_coords) - min(x_coords)) * (max(y_coords) - min(y_coords))
    # A = area = length * height
    areas.append(A)


''' 
ALL OF THIS COMMENTED OUT CODE BELONGS IN THE MAIN FOR LOOP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  # take dispersal list values and assign them to inds, spes, x_coords, y_coords
len_list = [len(inds), len(spes), len(x_coords), len(y_coords)]
  # get the length of inds, spes, x_coords and y_coords then assign the value to 
  # the variable of len_list
if min(len_list) != max(len_list):
  # if min does not equal to max then print
  print(len_list)
      
  # write data to file every 10 time steps
if x%25 == 0:
  # if 25 equal to 0 while running the the program 1000 time then gather data

    OUT = open(mydir + 'SimData/inds_data.csv', 'a+')
    outlist = str(inds).strip('[]') # in the list of inds strip all "[]" from 
                                    # the list then assigen it to the variable 
                                    # of oulis
    outlist = outlist.replace(" ", "") # Use the variable of outlist and 
                                       # replace(x, y) all " " with "" then 
                                   # assign the value back to outlist
    OUT.write(outlist)
    OUT.close()

    OUT = open(mydir + 'SimData/spes_data.csv', 'a+')
    outlist = str(spes).strip('[]') # in the list of spes strip all "[]" from 
                                    # the list then assigen it to the variable 
                                    # of oulist
    outlist = outlist.replace(" ", "") # Use the variable of outlist and 
                                       # replace(x, y) all " " with "" then 
                                       # assign the value back to outlist
    OUT.write(outlist)
    OUT.close()

    OUT = open(mydir + 'SimData/x_coords_data.csv', 'a+')
    outlist = str(x_coords).strip('[]') # in the list of x_coords strip all "[]" from 
                                    # the list then assigen it to the variable 
                                    # of oulist
    outlist = outlist.replace(" ", "") # Use the variable of outlist and 
                                       # replace(x, y) all " " with "" then 
                                       # assign the value back to outlist
    OUT.write(outlist)
    OUT.close()

    OUT = open(mydir + 'SimData/y_coords_data.csv', 'a+')
    outlist = str(y_coords).strip('[]') # in the list of y_coords strip all "[]" from 
                                    # the list then assigen it to the variable 
                                    # of oulist
    outlist = outlist.replace(" ", "") # Use the variable of outlist and 
                                       # replace(x, y) all " " with "" then 
                                       # assign the value back to outlist
    OUT.write(outlist)
    OUT.close()
'''


# Part 5 make figures (show or save to file)

fig = plt.figure()
# N vs. time
fig.add_subplot(2, 2, 1)
plt.plot(Ns, color = "c")
plt.xlabel()
plt.ylabel()
plt.yscale('log')


fig.add_subplot(2, 2, 2)
# S vs. time
plt.plot(Ss, color = "m")  
plt.xlabel()
plt.ylabel()
plt.yscale('log')


fig.add_subplot(2, 2, 3)
# area of occupied landscape vs. time (Does the area just keep increasing?)
plt.scatter(x_coords, y_coords, color = "0.5")
plt.xlabel()
plt.ylabel()


fig.add_subplot(2, 2, 4)
# immigration rate vs. time to extinction (how does immigration rate effect how long the community lasts?)
plt.scatter(m, gens, color = "1")
plt.xlabel()
plt.ylabel()

fig.show()
# plt.savefig()
