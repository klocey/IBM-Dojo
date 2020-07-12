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

plt.xlabel("Time")
plt.ylabel("Total abundance (N)")
plt.yscale('log')


fig.add_subplot(2, 2, 2)
for model in models:
    df2 = df[df['model'] == model]
    clr = df2['clr'].tolist()[0]
    plt.plot(df2['t'], df2['Healthy']/df2['N'], label = "Healthy", color = "red", linewidth=0.25, alpha=0.8)
    plt.plot(df2['t'], df2['Sick']/df2['N'], label = "Sick", color = "blue", linewidth=0.25, alpha=0.8)

plt.xlabel("Time")
plt.ylabel("Relative abundance")
#plt.yscale('log')

print("I just want to sleep")

plt.legend(loc='best', edgecolor='None', fontsize=8)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig(mydir + '/CEMs/figures/Fig1.png', dpi=400, bbox_inches = "tight")
#plt.close()

