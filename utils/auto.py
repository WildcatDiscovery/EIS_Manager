#AUTO FUNCTION
from tools import *
import logging
logging.getLogger().setLevel(logging.CRITICAL)
import math
def auto_fit(path, csv, save_fig = False):
    final_coeffs = []
    for i in range(len(csv)):
        mpt = mpt_data(path = path, data = [csv.iloc[i].name])
        if len((csv.iloc[i].mask_choice.strip('[')).strip('];')) == 1:
            mask_choice = mpt.fast_mask()
            masked_mpt = mpt_data(path = path, data = [csv.iloc[i].name], mask = mask_choice)

            if (csv.iloc[i].mask_choice.strip('[')).strip('];') == "1":
                if type((csv.iloc[i].recal_indices)) == str:
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
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
                else:
                    masked_mpt.guesser()
                final_coeffs.append(masked_mpt.guesser())
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "2":
                mask_choice = mpt.masker0()
                masked_mpt = mpt_data(path = path, data = [csv.iloc[i].name], mask = mask_choice)
                if type((csv.iloc[i].recal_indices)) == str:
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
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
                else:
                    #masked_mpt.guesser()
                    continue
                final_coeffs.append(masked_mpt.guesser())
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "3":
                mask_choice = mpt.masker()
                masked_mpt = mpt_data(path =  path, data = [csv.iloc[i].name], mask = mask_choice)
                if type((csv.iloc[i].recal_indices)) == str:
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
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
                #print(masked_mpt.guesser(save_fig = save_fig))
                final_coeffs.append(masked_mpt.guesser())
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "4":
                if type((csv.iloc[i].recal_indices)) == str:
                    pre_inds =(csv.iloc[i].recal_indices.strip('[')).strip(']').split(',') 
                    edited_inds = [int(i) for i in pre_inds]
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
                    mpt.guesser()
                #print(mpt.guesser(save_fig = save_fig))
                final_coeffs.append(mpt.guesser())
                mpt.mpt_plot(fitting = 'on', save_fig = True)
            else:
                print('bad masking choice')
        else:
            raw_window = [str(i) for i in (csv.iloc[i].mask_choice.strip('[')).strip('];').split(',')]
            mask_choice = mpt.window_masker([float(raw_window[0]),float(raw_window[1])], [float(raw_window[2]),float(raw_window[3])])
            masked_mpt = mpt_data(path =  path, data = [csv.iloc[i].name], mask = mask_choice)
            if (str(csv.iloc[i].recal_indices).strip('[')).strip(']') != 'nan':
                pre_inds =(str(csv.iloc[i].recal_indices).strip('[')).strip(']').split(',') 
                edited_inds = [int(i) for i in pre_inds]
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

                final_coeffs.append(masked_mpt.guesser())
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
            else:
                final_coeffs.append(masked_mpt.guesser())
                masked_mpt.mpt_plot(fitting = 'on', save_fig = True)
    
    for i in range(len(final_coeffs)-1):
        final_coeffs[0] = final_coeffs[0].append(final_coeffs[i+1])
    final_coeffs[0].drop(columns = ['fit_fs1', 'fit_fs2'], inplace = True)
    final_coeffs[0].to_csv(r"C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\utils\fitted_folder\\output.txt", sep = ",", index=False)