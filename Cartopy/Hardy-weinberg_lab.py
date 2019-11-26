from random import choice
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
AAM = 3
N = 28
R = 16
 
############################### Assumptions Met ###############################
for i in range(AAM):
    print('50/50')
    for i in range(N):
        beads = ['A','B']
        beads_ps = [0.5, 0.5]
        Beads_AB = np.random.choice(beads, size=2, replace=True, p=beads_ps)
        print(Beads_AB)
    print('42 A and 12 B')
    for i in range(N):
        beads = ['A','B']
        beads_ps = [0.7, 0.3]
        Beads_AB = np.random.choice(beads, size=2, replace=True, p=beads_ps)
        print(Beads_AB)    
    print('\n')
    
############################ Assortative Mating ###############################   

######################### Selection against recessive #########################
        
######################### Selection against dominant ##########################
        
####################### Selection against heterozygous ########################

############################### Genetic Drift #################################
        
#################################### Plot #####################################        
'''
ax = fig.add_subplot(111)
plt.plot(Hardy_Weinberg, N)
ax.set_xticklabels(['Floor', 'Table', 'Ground', 'Veg', 'Cushion'])
''' 
