import numpy as np

############################### lat and lon ####################################
curr_loc_x = 361736 
curr_loc_y = 1091250

sick_loc_x = 361730
sick_loc_y = 1091306

loc_H_x = 360928
loc_H_y = 1093627

################################ Treatment #####################################
tmt_d = np.sqrt((curr_loc_x - loc_H_x)**2+(curr_loc_y - loc_H_y)**2)
prob_tmt = 1000 / (1000 + tmt_d)
prob_tmt_pre = prob_tmt * 100

############################### Infection ######################################
inf_d = np.sqrt((curr_loc_x - sick_loc_x)**2+(curr_loc_y - sick_loc_y)**2)
prob_inf = 1000 / (1000 + inf_d)
prob_inf_pre = prob_inf * 100

############################### ???????? #######################################

############################# Print Function ###################################
print('Treatment Probability')
print(tmt_d)
print(prob_tmt_pre, "%")
print(prob_tmt)

print(" ")

print('Infection Probability')
print(inf_d)
print(prob_inf_pre, '%')
print(prob_inf)
