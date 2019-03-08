from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import os


mydir = os.path.expanduser('~/GitHub/IBM-Dojo')
df = pd.read_csv(mydir + '/CEMs/SimData/Compiled_Data.txt')


models = list(set(df['model'].tolist()))
print(models)

fig = plt.figure()

# N vs. time
fig.add_subplot(2, 2, 1)
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['Healthy'], label = "Healthy", color = "red", linewidth=0.25, alpha=0.8)
    plt.plot(df2['t'], df2['Sick'], label = "Sick", color = "blue", linewidth=0.25, alpha=0.8)

fig.add_subplot(2, 2, 2)
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['Healthy']/df2['N'], label = "Healthy", color = "red", linewidth=0.25, alpha=0.8)
    plt.plot(df2['t'], df2['Sick']/df2['N'], label = "Sick", color = "blue", linewidth=0.25, alpha=0.8)
'''r
22) we open a path called df then assigned it the name 'Model' then we gave it the
    variable of df2
23) this line determind the color of the line that well be on the graph
24) plot df with the list of 'T' which is time. df two well also have the number
    of indiividuals. color well be clr which is determind by 'm'. the with of 
    the line well be 0.25
'''

#plt.xlabel("Time")
#plt.ylabel("Total abundance (N)")
#plt.yscale('log')

'''
35) xlabel well have the name of time
36) ylabel well be named Total abundance (N)
37) y axis we be scaled to log
'''

plt.legend(loc='best', edgecolor='None', fontsize=8)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig(mydir + '/CEMs/figures/Fig1.png', dpi=400, bbox_inches = "tight")
#plt.close('all')

'''
we save the data that we are collecting as we are running that way we dont have 
any chance of lose the data for some reason
'''
