from tools import *
import pandas as pd
import numpy as np
import statistics as stat
import sys
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)
#Script to display the dataframe of a single mpt file

path = sys.argv[1]
data = sys.argv[2]
data_edit = data.strip('\n')
sys.argv[2] = "/" + data_edit
mask_choice = sys.argv[3]
data = sys.argv[2]

x_min = float(sys.argv[3])
x_max = float(sys.argv[4])

y_min = float(sys.argv[5])
y_max = float(sys.argv[6])

bad_inds = sys.argv[7]



pre_inds = bad_inds.strip('][').split(',') 
edited_inds = [int(i) for i in pre_inds]

def window_masker(self, x_window, y_window):
        adj_re = self.df[0][(self.df[0]['re']<x_window[1]) & (self.df[0]['re']>x_window[0])]
        adj_mpt = adj_re[(adj_re['im']<y_window[1]) & (adj_re['im']>y_window[0])]
        return [max(adj_mpt['f']), min(adj_mpt['f'])]
#This object is to collect the mask
ex_mpt = mpt_data(path, [data])

masker = window_masker(ex_mpt, x_window = [x_min, x_max], y_window = [y_min, y_max])
#This object is to actually fit on the dataframe
ex_mpt2 = mpt_data(path, [data],mask = masker)


for ind in edited_inds:
    if ind == "[":
        continue
    elif ind == "]":
        continue
    else:      
        if ind in ex_mpt2.df[0].index:  
            ex_mpt2.df[0] = ex_mpt2.df[0].drop(ind,axis=0)
        else:
            continue

#print(ex_mpt2.df[0][['re', 'im']])

#ex_mpt.mask = masker

#masked_mpt = mpt_data(path, [data], mask = masker)
#print('masked')
#print(ex_mpt2.df[0])
#print(masked_mpt.df[0])

#print(len(ex_mpt2.df[0]))
print(ex_mpt2.guesser())
#print(len(ex_mpt2.circuit_fit[0]))
for i in ex_mpt2.circuit_fit[0]:
        print(i.real, ", ", -i.imag)
ex_mpt2.mpt_plot(fitting = 'on')