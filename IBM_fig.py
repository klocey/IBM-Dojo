from __future__ import division
import numpy as np
from random import choice, uniform, randint
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt


mydir = os.path.expanduser('~/GitHub/IBM-Dojo')
df = pd.read_csv(mydir + '/SimData/Compiled_Data.txt')

models = list(set(df['model'].tolist()))


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
# S vs. time
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['S'], color = clr, linewidth=0.25, alpha=0.8)

plt.xlabel("Time")
plt.ylabel("Species richness (S)")
plt.yscale('log')


fig.add_subplot(2, 2, 3)
# area of occupied landscape vs. time (Does the area just keep increasing?)
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['area'], color = clr, linewidth=0.25, alpha=0.8)

plt.xlabel("Time")
plt.ylabel("Occupied area")
plt.yscale('log')


fig.add_subplot(2, 2, 4)
# immigration rate vs. time to extinction (how does immigration rate effect how long the community lasts?)
for model in models:
    df2 = df[df['model'] == model]
    df2 = df2[df2['extinct'] == True]
    if len(df2['extinct'].tolist()) == 0: continue
    clr = df2['clr'].tolist()[0]
    plt.scatter(df2['m'], df2['t'], c = clr, s = 10, alpha=0.4, linewidths=0.0)

plt.ylabel("Time to extinction")
plt.xlabel("Immigration Rate")


plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig(mydir + '/figures/Fig1.png', dpi=400, bbox_inches = "tight")
plt.close()
