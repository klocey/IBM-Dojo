from __future__ import division
from random import choice, uniform, randint

# Part 2 (below): define functions

def modelcolor(m):
    clr = str()
    if m <= 1: clr = 'darkred'
    elif m < 2: clr = 'red'
    elif m < 3: clr = 'orange'
    elif m < 4: clr = 'yellow'
    elif m < 5: clr = 'lawngreen'
    elif m < 6: clr = 'green'
    elif m < 7: clr = 'deepskyblue'
    elif m < 8: clr = 'blue'
    elif m < 9: clr = 'blueviolet'
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

def reproduce(inds, spes, x_coords, y_coords): #Made a function an called it reproduce assigned it the list of inds, spes, x_coords, y_coords

  i1 = list(inds) 
  s1 = list(spes) 
  x1 = list(x_coords) 
  y1 = list(y_coords) 

  '''
  44) list of inds and asignned it the variable of i1
  45) list of spes and asignned it the variable of i1
  46) list of x_coords and asignned it the variable of i1
  47) list of y_coords and asignned it the variable of i1
  we assigned the list new variable because we do not want them to point at the same data
  '''

  for i, val in enumerate(spes):# loop through val of spes
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
  60) list of spes is gonna be extend by val list
  61)  max1 is a unique ID; get the max number of inds and assign it to max1
  62) extend i1 by max1 which has assigned value of max(inds)

  '''

  return i1, s1, x1, y1 

  '''we return i1, s1, x1 and y1  as we dont want the came data from the other list
     they would both point at the same object
  '''

def death(inds, spes, x_coords, y_coords):
# made a function called death and assigned the list of inds, spes, x_coords and y_coords

  i1 = list(inds) 
  s1 = list(spes) 
  x1 = list(x_coords) 
  y1 = list(y_coords) 

  '''
  83) list of inds and assigne it the variable of i1
  84) list of spes and assigned it the variable of s1
  85) list of x_coords and assign it the variable of x1
  86) list of y_coords and assin it the variable of y1

  '''

  for val in spes:
    x = choice([0, 1])
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



def dispersal(inds, spes, x_coords, y_coords):
  for num in range(len(spes)): 
    i = randint(0, len(inds)-1) 
    x_coords[i] += uniform(-1, 1) 
    y_coords[i] += uniform(-1, 1) 
  return inds, spes, x_coords, y_coords

  '''
  117) for the range of spes use length for a loop
  118) randomly choose a number between 0 and the length of inds
  119) x_coords[i] += uniform(-1, 1) # += is a shortcut for x = x + y
  120) y_coords[i] += uniform(-1, 1) # += is a shortcut for y = x + y
  '''

def immigration(inds, spes, x_coords, y_coords, S, m):
  for i in range(m): # number of orgrainism immirgerating per gen
    s = randint(0, S)
    inds.append(max(inds)+1)
    spes.append(s)
    x_coords.append(uniform(min(x_coords), max(x_coords)))
    y_coords.append(uniform(min(y_coords), max(y_coords)))

  return inds, spes, x_coords, y_coords