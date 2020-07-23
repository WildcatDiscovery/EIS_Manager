#AUTO FUNCTION
from tools import *
import logging
logging.getLogger().setLevel(logging.CRITICAL)
import math
def auto_fit(path, csv, save_fig = False):
    for i in range(len(csv)):
        #print(i)
        mpt = mpt_data(path = path, data = [csv.iloc[i].name])
        print(mpt.data)
        if len((csv.iloc[i].mask_choice.strip('[')).strip('];')) == 1:
            mask_choice = mpt.fast_mask()
            masked_mpt = mpt_data(path = path, data = [csv.iloc[i].name], mask = mask_choice)
            #print(len(masked_mpt.df[0]))
            if (csv.iloc[i].mask_choice.strip('[')).strip('];') == "1":
                if type((csv.iloc[i].recal_indices)) == str:
                    #print(csv.iloc[i].recal_indices)
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
                    #print(edited_inds)
                    for ind in edited_inds:
                        if ind == "[":
                            continue
                        elif ind == "]":
                            continue
                        else:      
                            if ind in masked_mpt.df[0].index:  
                                masked_mpt.df[0] = masked_mpt.df[0].drop(ind,axis=0)
                            else:
                                continue
                    #print(len(masked_mpt.df[0]))
                else:
                    #print('guessing...')
                    continue
                print(masked_mpt.guesser(save_fig = save_fig))
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "2":
                mask_choice = mpt.masker0()
                masked_mpt = mpt_data(path = path, data = [csv.iloc[i].name], mask = mask_choice)
                if type((csv.iloc[i].recal_indices)) == str:
                    #print(csv.iloc[i].recal_indices)
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
                    #print(edited_inds)
                    for ind in edited_inds:
                        if ind == "[":
                            continue
                        elif ind == "]":
                            continue
                        else:      
                            if ind in masked_mpt.df[0].index:  
                                masked_mpt.df[0] = masked_mpt.df[0].drop(ind,axis=0)
                            else:
                                continue
                    #print(len(masked_mpt.df[0]))
                else:
                    #print('guessing...')
                    continue
                print(masked_mpt.guesser(save_fig = save_fig))
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "3":
                mask_choice = mpt.masker()
                masked_mpt = mpt_data(path =  path, data = [csv.iloc[i].name], mask = mask_choice)
                if type((csv.iloc[i].recal_indices)) == str:
                    #print(csv.iloc[i].recal_indices)
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
                    #print(edited_inds)
                    for ind in edited_inds:
                        if ind == "[":
                            continue
                        elif ind == "]":
                            continue
                        else:      
                            if ind in masked_mpt.df[0].index:  
                                masked_mpt.df[0] = masked_mpt.df[0].drop(ind,axis=0)
                            else:
                                continue
                    #print(len(masked_mpt.df[0]))
                else:
                    #print('guessing...')
                    continue
                print(masked_mpt.guesser(save_fig = save_fig))
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "4":
                if type((csv.iloc[i].recal_indices)) == str:
                    #print(csv.iloc[i].recal_indices)
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
                    #print(edited_inds)
                    for ind in edited_inds:
                        if ind == "[":
                            continue
                        elif ind == "]":
                            continue
                        else:      
                            if ind in masked_mpt.df[0].index:  
                                mpt.df[0] = mpt.df[0].drop(ind,axis=0)
                            else:
                                continue
                    #print(len(masked_mpt.df[0]))
                else:
                    #print('guessing...')
                    continue
                print(mpt.guesser(save_fig = save_fig))
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            else:
                print('bad masking choice')
        else:
            #print([str(i) for i in (csv.iloc[i].mask_choice.strip('[')).strip('];').split(',')])
            raw_window = [str(i) for i in (csv.iloc[i].mask_choice.strip('[')).strip('];').split(',')]
            #print(mpt.window_masker([raw_window[0],raw_window[1]], [raw_window[2],raw_window[3]]))
            mask_choice = mpt.window_masker([float(raw_window[0]),float(raw_window[1])], [float(raw_window[2]),float(raw_window[3])])
            masked_mpt = mpt_data(path =  path, data = [csv.iloc[i].name], mask = mask_choice)
            #print((str(csv.iloc[i].recal_indices).strip('[')).strip(']'))
            if (str(csv.iloc[i].recal_indices).strip('[')).strip(']') != 'nan':
                pre_inds =(str(csv.iloc[i].recal_indices).strip('[')).strip(']').split(',') 
                #print(pre_inds)
                edited_inds = [int(i) for i in pre_inds]
                #print(edited_inds)
                for ind in edited_inds:
                    if ind == "[":
                        continue
                    elif ind == "]":
                        continue
                    else:      
                        if ind in masked_mpt.df[0].index:  
                            masked_mpt.df[0] = masked_mpt.df[0].drop(ind,axis=0)
                        else:
                            continue
                print(masked_mpt.guesser(save_fig = save_fig))
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            else:
                print(masked_mpt.guesser(save_fig = save_fig))
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
        