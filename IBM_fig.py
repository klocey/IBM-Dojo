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

'''
22) we open a path called df then assigned it the name 'Model' then we gave it the
    variable of df2
23) this line determind the color of the line that well be on the graph
24) plot df with the list of 'T' which is time. df two well also have the number
    of indiividuals. color well be clr which is determind by 'm'. the with of 
    the line well be 0.25
'''

plt.xlabel("Time")
plt.ylabel("Total abundance (N)")
plt.yscale('log')

'''
35) xlabel well have the name of time
36) ylabel well be named Total abundance (N)
37) y axis we be scaled to log
'''


fig.add_subplot(2, 2, 2)
# S vs. time
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['S'], color = clr, linewidth=0.25, alpha=0.8)

'''
48) we open a path called df then assigned it the name 'Model' then we gave it the
    variable of df2
49) this line determind the color of the line that well be on the graph
50) plot df with the list of 'T' which is time. df two well also have the number
    of indiividuals. color well be clr which is determind by 'm'. the with of 
    the line well be 0.25
'''

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

    '''
    84) if the length of the list is greater then 0 keep running the program until 
        it reaches 0
    '''

plt.ylabel("Time to extinction")
plt.xlabel("Immigration Rate")


plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig(mydir + '/figures/Fig1.png', dpi=400, bbox_inches = "tight")
plt.close()

'''
we save the data that we are collecting as we are running that way we dont have 
any chance of lose the data for some reason
'''
