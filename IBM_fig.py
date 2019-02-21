from __future__ import division
import numpy as np
from random import choice, uniform, randint
import sys
import os
import matplotlib.pyplot as plt







# Part 5 make figures (show or save to file)

fig = plt.figure()
# N vs. time
fig.add_subplot(2, 2, 1)
plt.plot(Ns, color = "c")
plt.xlabel("Time")
plt.ylabel("Individuals")
plt.yscale('log')


fig.add_subplot(2, 2, 2)
# S vs. time
plt.plot(Ss, color = "m")  
plt.xlabel("Time")
plt.ylabel("Spes")
plt.yscale('log')


fig.add_subplot(2, 2, 3)
# area of occupied landscape vs. time (Does the area just keep increasing?)
plt.scatter(x_coords, y_coords, color = "0.5")
plt.xlabel("Time")
plt.ylabel("Area")


fig.add_subplot(2, 2, 4)
# immigration rate vs. time to extinction (how does immigration rate effect how long the community lasts?)
print(len(ms))
print(len(gens))
plt.scatter(ms, gens, color = "1")
plt.xlabel("Time")
plt.ylabel("Immigration Rate")


plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig(mydir + '/figures/2by2.png', dpi=400, bbox_inches = "tight")
plt.close()