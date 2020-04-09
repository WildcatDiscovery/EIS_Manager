from tools import *
import pandas as pd
import numpy as np
import statistics as stat
import sys
#Script to display the dataframe of a single mpt file

path = sys.argv[1]
data = sys.argv[2]
data_edit = data.strip('\n')
sys.argv[2] = "/" + data_edit
mask_choice = sys.argv[3]
data = sys.argv[2]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#print(sys.argv)

ex_mpt = mpt_data(path, [data])
#ex_mpt.mpt_plot()

if mask_choice == str(1):
    print(ex_mpt.fast_mask())
    masked_mpt = mpt_data(path, [data], mask = ex_mpt.fast_mask())
    print(masked_mpt.df[0][['f','re','im']])
   
elif mask_choice == str(2):
    print(ex_mpt.masker0())
    masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker0())
    print(masked_mpt.df[0][['f','re','im']])
elif mask_choice == str(3):
    print(ex_mpt.masker())
    masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker())
    print(masked_mpt.df[0][['f','re','im']])
else:
    print("Error, not a Masking Function")

