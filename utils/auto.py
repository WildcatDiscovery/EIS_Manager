#AUTO FUNCTION
#DRAFT LOTS OF STUFF TO EDIT HERE
import math
from tools import *
csv =pd.read_csv(r"C:\Users\cjang.WILDCAT\Desktop\eis\test", names = ['name', 'recal_indices', 'mask_choice'],index_col = 0, sep = " ", header = None)

for i in range(len(csv)):
    mpt = mpt_data(path = r'C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\data\\', data = [csv.iloc[i].name])
    #print(mpt.data)
    if len((csv.iloc[i].mask_choice.strip('[')).strip('];')) == 1:
        mask_choice = mpt.fast_mask()
        masked_mpt = mpt_data(path = r'C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\data\\', data = [csv.iloc[i].name], mask = mask_choice)
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
            print(masked_mpt.guesser())
        elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "2":
            mask_choice = mpt.masker0()
            masked_mpt = mpt_data(path =  r'C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\data\\', data = [csv.iloc[i].name], mask = mask_choice)
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
            print(masked_mpt.guesser())
        elif (csv.iloc[i].mask_choice.strip('[')).strip('];') == "3":
            mask_choice = mpt.masker()
            masked_mpt = mpt_data(path =  r'C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\data\\', data = [csv.iloc[i].name], mask = mask_choice)
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
            print(masked_mpt.guesser())
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
            print(mpt.guesser())
            print('here')
        else:
            print('bad masking choice')
    else:
        #print([float(i) for i in (csv.iloc[i].mask_choice.strip('[')).strip('];').split(',')])
        raw_window = [float(i) for i in (csv.iloc[i].mask_choice.strip('[')).strip('];').split(',')]
        #print(mpt.window_masker([raw_window[0],raw_window[1]], [raw_window[2],raw_window[3]]))
        mask_choice = mpt.window_masker([raw_window[0],raw_window[1]], [raw_window[2],raw_window[3]])
        masked_mpt = mpt_data(path =  r'C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\data\\', data = [csv.iloc[i].name], mask = mask_choice)
        if (csv.iloc[i].recal_indices.strip('[')).strip(']') != 'NaN':
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
        else:
            continue
        #print(len(masked_mpt.df[0]))
        #d = (masked_mpt.df[0])
        print(masked_mpt.guesser())