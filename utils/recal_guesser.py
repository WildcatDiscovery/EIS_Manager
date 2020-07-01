from tools import *
import pandas as pd
import numpy as np
import statistics as stat
import sys
#Script to display the dataframe of a single mpt file
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)
path = sys.argv[1]
data = sys.argv[2]
data_edit = data.strip('\n')
sys.argv[2] = "/" + data_edit
mask_choice = sys.argv[3]
data = sys.argv[2]
bad_inds = sys.argv[4]

#print(sys.argv)

ex_mpt = mpt_data(path, [data])

pre_inds = bad_inds.strip('][').split(',') 
edited_inds = [int(i) for i in pre_inds]
#print(edited_inds)
if mask_choice == str(1):
    masked_mpt = mpt_data(path, [data], mask = ex_mpt.fast_mask())
    for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
    print(masked_mpt.guesser())
    for i in masked_mpt.circuit_fit[0]:
            print(i.real, ", ", -i.imag)
elif mask_choice == str(2):
    masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker0())
    for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
    print(masked_mpt.guesser())
    for i in masked_mpt.circuit_fit[0]:
            print(i.real, ", ", -i.imag)
elif mask_choice == str(3):
    masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker())
    for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
    print(masked_mpt.guesser())
    for i in masked_mpt.circuit_fit[0]:
            print(i.real, ", ", -i.imag)
elif mask_choice == str(4):
    for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            ex_mpt.df[0] = ex_mpt.df[0].drop(ind)
    print(ex_mpt.guesser())
    for i in ex_mpt.circuit_fit[0]:
            print(i.real, ", ", -i.imag)
else:
    print("Incorrect Input")