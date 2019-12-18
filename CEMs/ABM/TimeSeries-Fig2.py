from __future__ import division
#import numpy as np
#from random import choice, uniform, randint
import pandas as pd
#import sys
import os
import matplotlib.pyplot as plt

import Main_ABM as ABM

mydir = os.path.expanduser('~/GitHub/IBM-Dojo')
df = pd.read_csv(mydir + '/SimData/Compiled_Data.txt')

models = list(set(df['model'].tolist()))

#age_groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

fig = plt.figure()

# N vs. time
fig.add_subplot(2, 2, 1)
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['N'], color = clr, linewidth=0.25, alpha=0.8)

plt.xlabel("Time")
plt.ylabel("Total abundance (N)")
plt.yscale('log')

fig.add_subplot(2, 2, 2)
# m/f vs. time
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]    
    plt.plot(df2['t'], df2['sex' == 'm']/df2['N'], label = "Male", color = "blue", linewidth=0.25, alpha=0.8)
    plt.plot(df2['t'], df2['sex' == 'f']/df2['N'], label = "Female", color = "pink", linewidth=0.25, alpha=0.8)
    
plt.xlabel("Time")
plt.ylabel("Male/Female Ratio")
#plt.yscale('log')


fig.add_subplot(2, 2, 3)
# area of occupied landscape vs. time (Does the area just keep increasing?)
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['home_chapters'], color = clr, linewidth=0.25, alpha=0.8)

plt.xlabel("Time")
plt.ylabel("Chapters")
plt.yscale('log')

fig.add_subplot(2, 2, 4)
# immigration rate vs. time to extinction (how does immigration rate effect how long the community lasts?)
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.hist(df2['age'], ABM.age_groups, histtype = 'bar', rwidth = 0.8)

plt.ylabel("frequency")
plt.xlabel("Age Groups")

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig(mydir + '/figures/Fig1.png', dpi=400, bbox_inches = "tight")
plt.close()
