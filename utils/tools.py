#ASSISTING FUNCTIONS FOR THE IMPEDANCE_DATA IPYTHON NOTEBOOK
#DERIVED FROM KRISTIAN KNUDSEN'S PYEIS REPO
#HELPING TO FIT POINTS FROM A NYQUIST PLOT IN THE FORM OF A MPT FILE

#IMPORT NESSECARY LIBRARIES
#Python dependencies

from __future__ import division
import pandas as pd
import numpy as np
from scipy.constants import codata
from scipy.optimize import curve_fit
import mpmath as mp
from lmfit import minimize, Minimizer, Parameters, Parameter, report_fit
import sys, traceback
import time
import random
import warnings
pd.options.mode.chained_assignment = None
import statistics as stat
import random
from os import listdir
from os.path import isfile, join
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


#Plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.use("Agg")
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import seaborn as sns
import matplotlib.ticker as mtick
mpl.rc('mathtext', fontset='stixsans', default='regular')
mpl.rcParams.update({'axes.labelsize':22})
mpl.rc('xtick', labelsize=16) 
mpl.rc('ytick', labelsize=16)
mpl.rc('legend',fontsize=14)

from scipy.constants import codata
F = codata.physical_constants['Faraday constant'][0]
Rg = codata.physical_constants['molar gas constant'][0]


pd.options.mode.chained_assignment = None


#USE THIS FOR COMMAND LINE TESTING
#>python3 -c "from tools import *; print(mpt_data(path = r'C:\Users\cjang.WILDCAT\Desktop\EIS_Manager\data\\', data = ['DE_49_9_30.mpt']).df_raw)"



#TAKEN FROM PYEIS LIBRARY
def extract_mpt(EIS_name):
    '''
    Extracting PEIS and GEIS data files from EC-lab '.mpt' format, coloums are renames following correct_text_EIS()
    
    Kristian B. Knudsen (kknu@berkeley.edu || kristianbknudsen@gmail.com)
    '''
    EIS_init = pd.read_csv(EIS_name, sep='\\', nrows=1,header=0,names=['err'], encoding='latin1') #findes line that states skiplines
    EIS_test_header_names = pd.read_csv(EIS_name, sep='\t', skiprows=int(EIS_init.err[0][18:-1])-1, encoding='latin1') #locates number of skiplines
    names_EIS = []
    for j in range(len(EIS_test_header_names.columns)):
        names_EIS.append(correct_text_EIS(EIS_test_header_names.columns[j])) #reads coloumn text
    return pd.read_csv(EIS_name, sep='\t', skiprows=int(EIS_init.err[0][18:-1]), names=names_EIS, encoding='latin1')

#TAKEN FROM PYEIS LIBRARY
def correct_text_EIS(text_header):
    '''Corrects the text of '*.mpt' and '*.dta' files into readable parameters without spaces, ., or /
    
    <E_we> = averaged Wew value for each frequency
    <I> = Averaged I values for each frequency
    |E_we| = module of Ewe
    |I_we| = module of Iwe
    Cs/F = Capacitance caluculated using an R+C (series) equivalent circuit
    Cp/F = Capacitance caluculated using an R-C (parallel) equivalent circuit
    Ref.:
        - EC-Lab User's Manual
    
    Kristian B. Knudsen (kknu@berkeley.edu || kristianbknudsen@gmail.com)
    '''
    if text_header == 'freq/Hz' or text_header == '  Freq(Hz)':
        return 'f'
    elif text_header == 'Re(Z)/Ohm' or text_header == "Z'(a)":
        return 're'
    elif text_header == '-Im(Z)/Ohm' or text_header == "Z''(b)":
        return 'im'
    elif text_header == '|Z|/Ohm':
        return 'Z_mag'
    elif text_header == 'Phase(Z)/deg':
        return 'Z_phase'
    elif text_header == 'time/s' or text_header == 'Time(Sec)':
        return 'times'
    elif text_header == '<Ewe>/V' or text_header == 'Bias':
        return 'E_avg'
    elif text_header == '<I>/mA':
        return 'I_avg'
    elif text_header == 'Cs/F':
        return 'Cs' ####
    elif text_header == 'Cp/F':
        return 'Cp'
    elif text_header == 'cycle number':
        return 'cycle_number'
    elif text_header == 'Re(Y)/Ohm-1':
        return 'Y_re'
    elif text_header == 'Im(Y)/Ohm-1':
        return 'Y_im'
    elif text_header == '|Y|/Ohm-1':
        return 'Y_mag'
    elif text_header == 'Phase(Y)/deg':
        return 'Y_phase'
    elif text_header == 'Time':
        return 'times'
    elif text_header == 'Freq':
        return 'f'
    elif text_header == 'Zreal':
        return 're'
    elif text_header == 'Zimag':
        return 'im'
    elif text_header == 'Zmod':
        return 'Z_mag'
    elif text_header == 'Vdc':
        return 'E_avg'
    elif text_header == 'Idc':
        return 'I_avg'
    elif text_header == 'I/mA':
        return 'ImA'
    elif text_header == 'Ewe/V':
        return 'EweV'
    elif text_header == 'half cycle':
        return 'half_cycle'
    elif text_header == 'Ns changes':
        return 'Ns_changes'
    else:
        return text_header
    
#BASIC ELEMENTS
def elem_Q(w,Q,n):
    '''
    Simulation Function: -Q-
    
    Inputs
    ----------
    w = Angular frequency [1/s]
    Q = Constant phase element [s^n/ohm]
    n = Constant phase elelment exponent [-]
    '''
    return 1/(Q*(w*1j)**n)
def cir_RQ(w, R='none', Q='none', n='none', fs='none'):
    '''
    Simulation Function: -RQ-
    Return the impedance of an Rs-RQ circuit. See details for RQ under cir_RQ_fit()
    
    Kristian B. Knudsen (kknu@berkeley.edu / kristianbknudsen@gmail.com)
    
    Inputs
    ----------
    w = Angular frequency [1/s]
    R = Resistance [Ohm]
    Q = Constant phase element [s^n/ohm]
    n = Constant phase elelment exponent [-]
    fs = Summit frequency of RQ circuit [Hz]
    '''
    if R == 'none':
        R = (1/(Q*(2*np.pi*fs)**n))
    elif Q == 'none':
        Q = (1/(R*(2*np.pi*fs)**n))
    elif n == 'none':
        n = np.log(Q*R)/np.log(1/(2*np.pi*fs))
    return (R/(1+R*Q*(w*1j)**n))


class mpt_data:
    def __init__(self, data, cycle='off', mask=['none','none'], gph_width = 6.4, gph_height = 4.8):
        self.data = data
        self.width = gph_width
        self.height = gph_height
        self.df_raw0 = []
        self.cycleno = []
        self.mask = mask
        self.counter = 0
        self.low_error = 0
        for j in range(len(data)):
            if data[j].find(".mpt") != -1: #file is a .mpt file
                self.df_raw0.append(extract_mpt(EIS_name=data[j])) #reads all datafiles
            else:
                print('Data file(s) could not be identified')

            self.cycleno.append(self.df_raw0[j].cycle_number)
            if np.min(self.cycleno[j]) <= np.max(self.cycleno[j-1]):
                if j > 0: #corrects cycle_number except for the first data file
                    self.df_raw0[j].update({'cycle_number': self.cycleno[j]+np.max(self.cycleno[j-1])}) #corrects cycle number

        self.df_raw = [i for i in self.df_raw0][0]
        self.df_raw = self.df_raw.assign(w = 2*np.pi*self.df_raw.f)

        #Masking data to each cycle
        self.df_pre = []
        self.df_limited = []
        self.df_limited2 = []
        self.df = []
        if mask == ['none','none'] and cycle == 'off':
            for i in range(len(self.df_raw.cycle_number.unique())): #includes all data
                self.df.append(self.df_raw[self.df_raw.cycle_number == self.df_raw.cycle_number.unique()[i]])                
        elif mask == ['none','none'] and cycle != 'off':
            for i in range(len(cycle)):
                self.df.append(self.df_raw[self.df_raw.cycle_number == cycle[i]]) #extracting dataframe for each cycle                                
        elif mask[0] != 'none' and mask[1] == 'none' and cycle == 'off':
            self.df_pre = self.df_raw.mask(self.df_raw.f > mask[0])
            self.df_pre.dropna(how='all', inplace=True)
            for i in range(len(self.df_pre.cycle_number.unique())): #Appending data based on cycle number
                self.df.append(self.df_pre[self.df_pre.cycle_number == self.df_pre.cycle_number.unique()[i]])
        elif mask[0] != 'none' and mask[1] == 'none' and cycle != 'off': # or [i for i, e in enumerate(mask) if e == 'none'] == [0]
            self.df_limited = self.df_raw.mask(self.df_raw.f > mask[0])
            for i in range(len(cycle)):
                self.df.append(self.df_limited[self.df_limited.cycle_number == cycle[i]])
        elif mask[0] == 'none' and mask[1] != 'none' and cycle == 'off':
            self.df_pre = self.df_raw.mask(self.df_raw.f < mask[1])
            self.df_pre.dropna(how='all', inplace=True)
            for i in range(len(self.df_raw.cycle_number.unique())): #includes all data
                self.df.append(self.df_pre[self.df_pre.cycle_number == self.df_pre.cycle_number.unique()[i]])
        elif mask[0] == 'none' and mask[1] != 'none' and cycle != 'off': 
            self.df_limited = self.df_raw.mask(self.df_raw.f < mask[1])
            for i in range(len(cycle)):
                self.df.append(self.df_limited[self.df_limited.cycle_number == cycle[i]])
        elif mask[0] != 'none' and mask[1] != 'none' and cycle != 'off':
            self.df_limited = self.df_raw.mask(self.df_raw.f < mask[1])
            self.df_limited2 = self.df_limited.mask(self.df_raw.f > mask[0])
            for i in range(len(cycle)):
                self.df.append(self.df_limited[self.df_limited2.cycle_number == cycle[i]])
        elif mask[0] != 'none' and mask[1] != 'none' and cycle == 'off':
            self.df_limited = self.df_raw.mask(self.df_raw.f < mask[1])
            self.df_limited2 = self.df_limited.mask(self.df_raw.f > mask[0])
            for i in range(len(self.df_raw.cycle_number.unique())):
                self.df.append(self.df_limited[self.df_limited2.cycle_number == self.df_raw.cycle_number.unique()[i]])
        else:
            print('__init__ error (#2)')
    
    #DEFINE SIZE OF GRAPH
    #BE CAREFUL AS THIS DOESN'T DETERMINE THE DIMENSIONS OF THE WINDOW
    #THIS ONLY SETS THE DIMENSIONS OF THE SIZE OF THE WINDOW
    #ACTUAL GRAPH DATA DIMENSIONS CAN BE ADJUSTED IN THE PLOTTING FUNCTION
    def set_gph_width(self, new_width):
        self.width = new_width
        return
    
    def set_gph_height(self, new_height):
        self.height = new_height
        return

    def set_new_gph_dims(self, new_width, new_height):
        self.set_gph_width(new_width)
        self.set_gph_height(new_height)
        return
    
    def fast_mask(self):
        skeleton = self.df_raw.iloc[:,0:3]
        re_mid, im_mid  = np.mean(skeleton['re']), np.mean(skeleton['im'])
        a = skeleton[abs(skeleton['re']) <= re_mid * .5]
        b = skeleton[abs(skeleton['im']) <= im_mid * .5]
        c = pd.concat([a, b]).drop_duplicates()
        return [c['f'].max(), c['f'].min()]

    def masker0(self):
        skeleton = self.df_raw.iloc[:,0:3]
        re_lim, im_lim  = max(skeleton['re']) * .6, max(skeleton['im'] * .6)
        a = skeleton[(skeleton['re']) <= re_lim]
        b = skeleton[(skeleton['im']) <= im_lim]
        c = pd.concat([a, b]).drop_duplicates()

        return [max(c['f']), min(c['f'])]

    def masker(self, num_bins = 5):

        c = self.df_raw.iloc[:,0:3]
        res = []
        ims = []

        for i in pd.cut(c['re'], num_bins):
            res.append(i)
        for i in pd.cut(c['im'], num_bins):
            ims.append(i)
        #print('res', res)
        #print('ims', ims)
        d = c[(c['re'] >=stat.mode(res).left) & (c['re'] <= (stat.mode(res).right + (stat.mode(res).right - stat.mode(res).left)))]
        #print(stat.mode(res).left -  stat.mode(res).right)
        f = d[(d['im'] >=stat.mode(ims).left) & (d['im'] <= (stat.mode(ims).right + (stat.mode(ims).right - stat.mode(ims).left)))]
        #print(stat.mode(ims).left - stat.mode(ims).right)
        return [max(f['f']), min(f['f'])]

    def window_masker(self, x_window, y_window):
        adj_re = self.df_raw[(self.df_raw['re']<x_window[1]) & (self.df_raw['re']>x_window[0])]
        adj_mpt = adj_re[(adj_re['im']<y_window[1]) & (adj_re['im']>y_window[0])]
        return [max(adj_mpt['f']), min(adj_mpt['f'])]
    
    #PLOTTING FUNCTION
    def mpt_plot(self, fitting='off', rr='off', legend='on', x_window = 'none', y_window = 'none', save_fig = False, prettify = False):
        
        #Figure Initialization
        
        fig = plt.figure(dpi=120, figsize = [15, 25], facecolor='w', edgecolor='w')
        fig.subplots_adjust(left=0.1, right=0.95, hspace=0.5, bottom=0.1, top=0.95)
        ax = fig.add_subplot(211, aspect='equal')
        ax.tick_params(axis='both', which='major', labelsize=20)
        ax.tick_params(axis='both', which='minor', labelsize=20)
        ### Figure specifics
        if legend == 'on': 
            ax.legend(loc='best', fontsize=12, frameon=False)
        if x_window != 'none':
            ax.set_xlim(x_window[0], x_window[1])
        if y_window != 'none':
            ax.set_ylim(y_window[0], y_window[1])
        
        #Color initialization
        colors = sns.color_palette("colorblind", n_colors=len(self.df))
        colors_real = sns.color_palette("Blues", n_colors=len(self.df)+2)
        colors_imag = sns.color_palette("Oranges", n_colors=len(self.df)+2)
    
        #Label functions
        self.label_re_1 = []
        self.label_im_1 = []
        self.label_cycleno = []
        if legend == 'on':
            for i in range(len(self.df)):
                self.label_re_1.append("Z' (#"+str(i+1)+")")
                self.label_im_1.append("Z'' (#"+str(i+1)+")")
                self.label_cycleno.append('#'+str(i+1))
        elif legend == 'potential':
            for i in range(len(self.df)):
                self.label_re_1.append("Z' ("+str(np.round(np.average(self.df[i].E_avg), 2))+' V)')
                self.label_im_1.append("Z'' ("+str(np.round(np.average(self.df[i].E_avg), 2))+' V)')
                self.label_cycleno.append(str(np.round(np.average(self.df[i].E_avg), 2))+' V')
        ### Nyquist Plot
        ax.set_title(self.data)
        if prettify:
            ax.set_xlabel("Z' [$\Omega$]",fontsize=40)
            ax.set_ylabel("-Z'' [$\Omega$]",fontsize=40)
            ax.plot(self.df[0].re/1000, self.df[0].im/1000, marker='o', ms=4, lw=2, color=colors[i], ls='-', markersize = 20, label='nvyquist_data')
        else:
            ax.set_xlabel("Z' [$\Omega$]",fontsize=40)
            ax.set_ylabel("-Z'' [$\Omega$]",fontsize=40)
            ax.plot(self.df[0].re, self.df[0].im, marker='o', lw=2, color=colors[i], ls='-', markersize = 8, label='nvyquist_data')
        if fitting == 'on':
            real = []
            imag = []
            for i in self.circuit_fit[0]:
                if prettify:
                    real.append(i.real/1000)
                    imag.append(-i.imag/1000)
                else:
                    real.append(i.real)
                    imag.append(-i.imag)
            ax.plot(real, imag, color = 'red', markersize = 20, label='fitted')
        plt.show()
        ax.legend()
        if save_fig:
            if fitting == "on":
                fig.savefig(r"C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\utils\fitted_folder\\"+self.data[0].strip('.mpt')+'_fitted.png')
            else:
                fig.savefig(r"C:\Users\cjang.WILDCAT\Desktop\eis\EIS_Manager\uploads\\"+self.data[0].strip('.mpt')+'.png')

    #FITTING THE FREQUENCY ONTO THE GRAPH. FLIP SWITCH ON PLOT FUNCT TO DISPLAY
    def mpt_fit(self, params, circuit, weight_func='modulus', nan_policy='raise', maxfev = 10):
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        self.Fit = []
        self.circuit_fit = []
        self.fit_E = []
        for i in range(len(self.df)):
            #for ix in range(len(self.df[i].w.values)):
             #   print(self.df[i].re.values[ix], self.df[i].im.values[ix])
            #print(len(self.df[i].w.values), len(self.df[i].re.values), len(self.df[i].im.values))
            fitted_mpt_data = minimize(self.leastsq_errorfunc, params, method='leastsq', args=(self.df[i].w.values, self.df[i].re.values, self.df[i].im.values, circuit, weight_func), nan_policy=nan_policy, maxfev=maxfev)
            self.Fit.append(fitted_mpt_data)
            #print(report_fit(self.Fit[i]))
            self.low_error = self.Fit[i].chisqr
            print("CHI-SQ ERROR: ", self.Fit[i].chisqr)
            #print("PARAMS", self.Fit[i].params)
            self.fit_E.append(np.average(self.df[i].E_avg))
        if circuit == 'R-RQ-Q':
            self.fit_Rs = []
            self.fit_n = []
            self.fit_R1 = []
            self.fit_n1 = []
            self.fit_Q = []
            self.fit_fs1 = []
            self.fit_Q1 = []
            for i in range(len(self.df)):
                if "'fs1'" in str(self.Fit[i].params.keys()):
                    self.circuit_fit.append(cir_RsRQQ(w=self.df[i].w, Rs=self.Fit[i].params.get('Rs').value, n=self.Fit[i].params.get('n').value, R1=self.Fit[i].params.get('R1').value, Q=self.Fit[i].params.get('Q').value, n1=self.Fit[i].params.get('n1').value, fs1=self.Fit[i].params.get('fs1').value))
                    self.fit_Rs.append(self.Fit[i].params.get('Rs').value)
                    self.fit_Q.append(self.Fit[i].params.get('Q').value)
                    self.fit_n.append(self.Fit[i].params.get('n').value)
                    self.fit_R1.append(self.Fit[i].params.get('R1').value)
                    self.fit_n1.append(self.Fit[i].params.get('n1').value)
                    self.fit_fs1.append(self.Fit[i].params.get('fs1').value)
        elif circuit == 'R-RQ-RQ':
            self.fit_Rs = []
            self.fit_R = []
            self.fit_n = []
            self.fit_R2 = []
            self.fit_n2 = []
            self.fit_fs = []
            self.fit_fs2 = []
            self.fit_Q = []
            self.fit_Q2 = []
            for i in range(len(self.df)):
                self.circuit_fit.append(cir_RsRQRQ(w=self.df[i].w, Rs=self.Fit[i].params.get('Rs').value, R=self.Fit[i].params.get('R1').value, n=self.Fit[i].params.get('n').value, Q=self.Fit[i].params.get('Q1').value, R2=self.Fit[i].params.get('R2').value, n2=self.Fit[i].params.get('n2').value, Q2=self.Fit[i].params.get('Q2').value))
                self.fit_Rs.append(self.Fit[i].params.get('Rs').value)
                self.fit_R.append(self.Fit[i].params.get('R1').value)
                self.fit_n.append(self.Fit[i].params.get('n').value)
                self.fit_Q.append(self.Fit[i].params.get('Q1').value)
                self.fit_R2.append(self.Fit[i].params.get('R2').value)
                self.fit_n2.append(self.Fit[i].params.get('n2').value)
                self.fit_Q2.append(self.Fit[i].params.get('Q2').value)
        elif circuit == 'R-RQ-RQ-Q':
            self.fit_Rs = []
            self.fit_R1 = []
            self.fit_n1 = []
            self.fit_R2 = []
            self.fit_n2 = []
            self.fit_fs1 = []
            self.fit_fs2 = []
            self.fit_Q = []
            self.fit_Q1 = []
            self.fit_Q2 = []
            self.fit_n = []
            for i in range(len(self.df)):
                if "'fs1'" in str(self.Fit[i].params.keys()) and "'fs2'" in str(self.Fit[i].params.keys()) and "'Q'" in str(self.Fit[i].params.keys()):
                    self.circuit_fit.append(cir_RsRQRQQ(w=self.df[i].w, Rs=self.Fit[i].params.get('Rs').value, Q=self.Fit[i].params.get('Q').value, n=self.Fit[i].params.get('n').value, R1=self.Fit[i].params.get('R1').value, Q1='none', n1=self.Fit[i].params.get('n1').value, fs1=self.Fit[i].params.get('fs1').value, R2=self.Fit[i].params.get('R2').value, Q2='none', n2=self.Fit[i].params.get('n2').value, fs2=self.Fit[i].params.get('fs2').value))
                    self.fit_Rs.append(self.Fit[i].params.get('Rs').value)
                    self.fit_R1.append(self.Fit[i].params.get('R1').value)
                    self.fit_n1.append(self.Fit[i].params.get('n1').value)
                    self.fit_fs1.append(self.Fit[i].params.get('fs1').value)
                    self.fit_R2.append(self.Fit[i].params.get('R2').value)
                    self.fit_n2.append(self.Fit[i].params.get('n2').value)
                    self.fit_fs2.append(self.Fit[i].params.get('fs2').value)
                    self.fit_Q.append(self.Fit[i].params.get('Q').value)
                    self.fit_n.append(self.Fit[i].params.get('n').value)
                elif "'Q1'" in str(self.Fit[i].params.keys()) and "'Q2'" in str(self.Fit[i].params.keys()) and "'Q'" in str(self.Fit[i].params.keys()):
                    self.circuit_fit.append(cir_RsRQRQQ(w=self.df[i].w, Rs=self.Fit[i].params.get('Rs').value, Q=self.Fit[i].params.get('Q').value, n=self.Fit[i].params.get('n').value, R1=self.Fit[i].params.get('R1').value, Q1=self.Fit[i].params.get('Q1').value, n1=self.Fit[i].params.get('n1').value, fs1='None', R2=self.Fit[i].params.get('R2').value, Q2=self.Fit[i].params.get('Q2').value, n2=self.Fit[i].params.get('n2').value, fs2='None'))
                    self.fit_Rs.append(self.Fit[i].params.get('Rs').value)
                    self.fit_R1.append(self.Fit[i].params.get('R1').value)
                    self.fit_n1.append(self.Fit[i].params.get('n1').value)
                    self.fit_Q1.append(self.Fit[i].params.get('Q1').value)
                    self.fit_R2.append(self.Fit[i].params.get('R2').value)
                    self.fit_n2.append(self.Fit[i].params.get('n2').value)
                    self.fit_Q2.append(self.Fit[i].params.get('Q2').value)
                    self.fit_Q.append(self.Fit[i].params.get('Q').value)
                    self.fit_n.append(self.Fit[i].params.get('n').value)
                else:
                    print('Not valid')
        else:
            print('Circuit was not properly defined, see details described in definition')
            
    def leastsq_errorfunc(self, params, w, re, im, circuit, weight_func = 'modulus'):
        if circuit == 'R-RQ-RQ':
            re_fit = cir_RsRQRQ_fit(params, w).real
            im_fit = -cir_RsRQRQ_fit(params, w).imag
        elif circuit == 'R-RQ-Q':
            re_fit = cir_RsRQQ_fit(params, w).real
            im_fit = -cir_RsRQQ_fit(params, w).imag
        elif circuit == 'R-RQ-RQ2':
            re_fit = cir_RsRQRQ2_fit(params, w).real
            im_fit = -cir_RsRQRQ2_fit(params, w).imag
        elif circuit == 'R-RQ-RQ-Q':
            re_fit = cir_RsRQRQQ_fit(params, w).real
            im_fit = -cir_RsRQRQQ_fit(params, w).imag
        else:
            print('Circuit is not defined in leastsq_errorfunc()')

        error = ([(re-re_fit)**2, (im-im_fit)**2]) #sum of squares
        
        #Different Weighing options, see Lasia
        if weight_func == 'modulus':
            weight = [1/((re_fit**2 + im_fit**2)**(1/2)), 1/((re_fit**2 + im_fit**2)**(1/2))]
        elif weight_func == 'proportional':
            weight = [1/(re_fit**2), 1/(im_fit**2)]
        elif weight_func == 'unity':
            unity_1s = []
            for k in range(len(re)):
                unity_1s.append(1) #makes an array of [1]'s, so that the weighing is == 1 * sum of squres.
            weight = [unity_1s, unity_1s]
        else:
            print('weight not defined in leastsq_errorfunc()')
        
        S = np.array(weight) * error #weighted sum of squares 
        return S
    
    #Updated Guesser
    def guesser(self, circuit = 'R-RQ-RQ-Q', csv_container = None, no_of_fits = 100, save_fig = False):
        start = time.time()
        print('running on ', sys.version)
        if circuit == 'R-RQ-RQ-Q':
            init_guesses = []
            param_list = []
            for i in range(no_of_fits):
                #print(i)
                Rs_guess = min(self.df[0]['re'])
                R1_guess = max(self.df[0]['re'])//4
                n1_guess = random.uniform(0, 1)
                q1_guess = random.uniform(0, .001)
                R2_guess = 2*max(self.df[0]['re'])//4
                n2_guess = random.uniform(0, 1)
                q2_guess = random.uniform(0, .001)
                Q3_guess = random.uniform(0, .001)
                n3_guess = random.uniform(0, 1)
                params = Parameters()
                params.add('Rs', value=Rs_guess, min=Rs_guess*.001, max=Rs_guess*10)
                params.add('R1', value=R1_guess, min=R1_guess*.001, max=R1_guess*10)
                params.add('n1', value=n1_guess, min=0, max=1)
                #params.add('fs1', value=fs1_guess, min=10**-2, max=10**10)
                params.add('Q1', value=q1_guess, min=0, max=.001)
                params.add('R2', value=R2_guess, min=R2_guess*.001, max=R2_guess*10)
                params.add('n2', value=n2_guess, min=.01, max=1)
                #params.add('fs2', value=fs2_guess, min=fs2_guess**.1, max=10**10)
                params.add('Q2', value=q2_guess, min=0, max=.001)
                params.add('Q', value=Q3_guess, min=0, max=.001)
                params.add('n', value=n3_guess, min=.01, max=1)
                param_list.append(params)
                self.mpt_fit(params, circuit = 'R-RQ-RQ-Q', maxfev = 500)
                init_guesses.append(self.low_error)
            params = param_list[init_guesses.index(min(init_guesses))]
            self.mpt_fit(params, circuit = 'R-RQ-RQ-Q',maxfev = 1000)
            #self.mpt_plot(fitting = 'on', save_fig = save_fig)
            self.fitted = pd.DataFrame({'file':self.data,
                        'fit_Rs':self.fit_Rs,
                    "fit_R1":self.fit_R1,
                    "fit_n1":self.fit_n1,
                    "fit_fs1":np.nan,
                    "fit_Q1":self.fit_Q1,                   
                    "fit_R2":self.fit_R2,
                    "fit_n2":self.fit_n2,
                    "fit_fs2":np.nan,
                    "fit_Q2":self.fit_Q2,
                    "fit_Q3":self.fit_Q,
                    "fit_n3":self.fit_n,})
            out_name = 'fitted_' + self.data[0][:-4]
            end = time.time()
            print('time to calculate: ',end - start, ' seconds')
            if csv_container:
                self.fitted.to_csv(csv_container+out_name, sep='\t')
                return self.fitted
            self.mpt_plot(fitting = "on")
            return self.fitted
        elif circuit == 'R-RQ-RQ':
            init_guesses = []
            param_list = []
            for i in range(no_of_fits):
                #print(i)
                Rs_guess = min(self.df[0]['re'])
                R1_guess = max(self.df[0]['re'])//4
                n1_guess = random.uniform(0, 1)
                q1_guess = random.uniform(0, .001)
                R2_guess = 2*max(self.df[0]['re'])//4
                n2_guess = random.uniform(0, 1)
                q2_guess = random.uniform(0, .001)
                #Q3_guess = random.uniform(0, .001)
                n3_guess = random.uniform(0, 1)
                params = Parameters()
                params.add('Rs', value=Rs_guess, min=Rs_guess*.001, max=Rs_guess*10)
                params.add('R1', value=R1_guess, min=R1_guess*.001, max=R1_guess*10)
                params.add('n1', value=n1_guess, min=0, max=1)
                #params.add('fs1', value=fs1_guess, min=10**-2, max=10**10)
                params.add('Q1', value=q1_guess, min=0, max=.001)
                params.add('R2', value=R2_guess, min=R2_guess*.001, max=R2_guess*10)
                params.add('n2', value=n2_guess, min=.01, max=1)
                #params.add('fs2', value=fs2_guess, min=fs2_guess**.1, max=10**10)
                params.add('Q2', value=q2_guess, min=0, max=.001)
                #params.add('Q', value=Q3_guess, min=0, max=.001)
                params.add('n', value=n3_guess, min=.01, max=1)
                param_list.append(params)
                self.mpt_fit(params, circuit = 'R-RQ-RQ', maxfev = 500)
                init_guesses.append(self.low_error)
            params = param_list[init_guesses.index(min(init_guesses))]
            self.mpt_fit(params, circuit = 'R-RQ-RQ',maxfev = 1000)
            #self.mpt_plot(fitting = 'on', save_fig = save_fig)
            self.fitted = pd.DataFrame({'file':self.data,
                    'fit_Rs':self.fit_Rs,
                    "fit_R1":self.fit_R,
                    "fit_n1":self.fit_n,
                    "fit_Q1":self.fit_Q,                   
                    "fit_R2":self.fit_R2,
                   "fit_n2":self.fit_n2,
                    "fit_Q2":self.fit_Q2})
            out_name = 'fitted_' + self.data[0][:-4]
            end = time.time()
            print('time to calculate: ',end - start, ' seconds')
            if csv_container:
                self.fitted.to_csv(csv_container+out_name, sep='\t')
                return self.fitted
            self.mpt_plot(fitting = "on")
            return self.fitted
    
    #Guess and Plot; who knows if i'll use it
    def guess_and_plot(self, csv_container = None, mask = None):
        if mask:
            masked_mpt = mpt_data(self.data, mask = mask)
            masked_mpt.guesser()
            masked_mpt.mpt_plot(fitting = 'on')
        else:
            self.guesser()
            self.mpt_plot(fitting = 'on')

def cir_RsRQQ_fit(params, w):
    Rs = params['Rs']
    Q = params['Q']
    n = params['n']
    Z_Q = 1/(Q*(w*1j)**n)

    if str(params.keys())[10:].find("R1") == -1: #if R == 'none':
        Q1 = params['Q1']
        n1 = params['n1']
        fs1 = params['fs1']
        R1 = (1/(Q1*(2*np.pi*fs1)**n1))
    if str(params.keys())[10:].find("Q1") == -1: #elif Q == 'none':
        R1 = params['R1']
        n1 = params['n1']
        fs1 = params['fs1']
        Q1 = (1/(R1*(2*np.pi*fs1)**n1))
    if str(params.keys())[10:].find("n1") == -1: #elif n == 'none':
        R1 = params['R1']
        Q1 = params['Q1']
        fs1 = params['fs1']
        n1 = np.log(Q1*R1)/np.log(1/(2*np.pi*fs1))
    if str(params.keys())[10:].find("fs1") == -1: #elif fs == 'none':
        R1 = params['R1']
        n1 = params['n1']
        Q1 = params['Q1']
    Z_RQ = (R1/(1+R1*Q1*(w*1j)**n1))
    
    return Rs + Z_RQ + Z_Q


def cir_RsRQRQ_fit(params, w):
    '''
    Fit Function: -Rs-RQ-RQ-
    Return the impedance of an Rs-RQ circuit. See details under cir_RsRQRQ()
    
    Kristian B. Knudsen (kknu@berkeley.edu / kristianbknudsen@gmail.com)
    '''
    R = params['R1']
    Q = params['Q1']
    n = params['n']
    R2 = params['R2']
    Q2 = params['Q2']
    n2 = params['n2']

    Rs = params['Rs']
    return Rs + (R/(1+R*Q*(w*1j)**n)) + (R2/(1+R2*Q2*(w*1j)**n2))

def cir_RsRQRQ2_fit(params, w):
    '''
    Fit Function: -Rs-RQ-RQ-
    Return the impedance of an Rs-RQ circuit. See details under cir_RsRQRQ()
    
    Kristian B. Knudsen (kknu@berkeley.edu / kristianbknudsen@gmail.com)
    '''
    if str(params.keys())[10:].find("'R'") == -1: #if R == 'none':
        Q = params['Q']
        n = params['n']
        fs = params['fs']
        R = (1/(Q*(2*np.pi*fs)**n))
    if str(params.keys())[10:].find("'Q'") == -1: #elif Q == 'none':
        R = params['R']
        n = params['n']
        fs = params['fs']
        Q = (1/(R*(2*np.pi*fs)**n))
    if str(params.keys())[10:].find("'n'") == -1: #elif n == 'none':
        R = params['R']
        Q = params['Q']
        fs = params['fs']
        n = np.log(Q*R)/np.log(1/(2*np.pi*fs))
    if str(params.keys())[10:].find("'fs'") == -1: #elif fs == 'none':
        R = params['R']
        Q = params['Q']
        n = params['n']

    if str(params.keys())[10:].find("'R2'") == -1: #if R == 'none':
        Q2 = params['Q2']
        n2 = params['n2']
        fs2 = params['fs2']
        R2 = (1/(Q2*(2*np.pi*fs2)**n2))
    if str(params.keys())[10:].find("'Q2'") == -1: #elif Q == 'none':
        R2 = params['R2']
        n2 = params['n2']
        fs2 = params['fs2']
        Q2 = (1/(R2*(2*np.pi*fs2)**n2))
    if str(params.keys())[10:].find("'n2'") == -1: #elif n == 'none':
        R2 = params['R2']
        Q2 = params['Q2']
        fs2 = params['fs2']
        n2 = np.log(Q2*R2)/np.log(1/(2*np.pi*fs2))
    if str(params.keys())[10:].find("'fs2'") == -1: #elif fs == 'none':
        R2 = params['R2']
        Q2 = params['Q2']
        n2 = params['n2']

    Rs = params['Rs']
    return Rs + cir_RQ(w, R=R, Q=Q, n=n, fs=fs) + cir_RQ(w, R=R2, Q=Q2, n=n2, fs=fs2)

def cir_RsRQRQQ_fit(params, w):
    '''
    Fit Function: -Rs-RQ-RQ-Q-
    Return the impedance of an Rs-RQ circuit. See details under cir_RsRQRQ()
    
    Kristian B. Knudsen (kknu@berkeley.edu / kristianbknudsen@gmail.com)
    '''
    if str(params.keys())[10:].find("'R1'") == -1: #if R == 'none':
        Q1 = params['Q1']
        n1 = params['n1']
        fs1 = params['fs1']
        R1 = (1/(Q1*(2*np.pi*fs1)**n1))
    if str(params.keys())[10:].find("'Q1'") == -1: #elif Q == 'none':
        R1 = params['R1']
        n1 = params['n1']
        fs1 = params['fs1']
        Q1 = (1/(R1*(2*np.pi*fs1)**n1))
    if str(params.keys())[10:].find("'n1'") == -1: #elif n == 'none':
        R1 = params['R1']
        Q1 = params['Q1']
        fs1 = params['fs1']
        n1 = np.log(Q1*R1)/np.log(1/(2*np.pi*fs1))
    if str(params.keys())[10:].find("'fs1'") == -1: #elif fs == 'none':
        R1 = params['R1']
        Q1 = params['Q1']
        n1 = params['n1']
        fs1 = 'None'

    if str(params.keys())[10:].find("'R2'") == -1: #if R == 'none':
        Q2 = params['Q2']
        n2 = params['n2']
        fs2 = params['fs2']
        R2 = (1/(Q2*(2*np.pi*fs2)**n2))
    if str(params.keys())[10:].find("'Q2'") == -1: #elif Q == 'none':
        R2 = params['R2']
        n2 = params['n2']
        fs2 = params['fs2']
        Q2 = (1/(R2*(2*np.pi*fs2)**n2))
    if str(params.keys())[10:].find("'n2'") == -1: #elif n == 'none':
        R2 = params['R2']
        Q2 = params['Q2']
        fs2 = params['fs2']
        n2 = np.log(Q2*R2)/np.log(1/(2*np.pi*fs2))
    if str(params.keys())[10:].find("'fs2'") == -1: #elif fs == 'none':
        R2 = params['R2']
        Q2 = params['Q2']
        n2 = params['n2']
        fs2 = 'none'
    Rs = params['Rs']
    Q = params['Q']
    n = params['n']
    return Rs + cir_RQ(w, R=R1, Q=Q1, n=n1, fs=fs1) + cir_RQ(w, R=R2, Q=Q2, n=n2, fs=fs2) + elem_Q(w,Q,n)

def cir_RsRQQ(w, Rs, Q, n, R1='none', Q1='none', n1='none', fs1='none'):
    '''
    Simulation Function: -Rs-RQ-Q-
    
    Inputs
    ----------
    w = Angular frequency [1/s]
    Rs = Series Resistance [ohm]
    
    R1 = Resistance in (RQ) circuit [ohm]
    Q1 = Constant phase element in (RQ) circuit [s^n/ohm]
    n1 = Constant phase elelment exponent in (RQ) circuit [-]
    fs1 = Summit frequency of RQ circuit [Hz]
    Q = Constant phase element of series Q [s^n/ohm]
    n = Constant phase elelment exponent of series Q [-]
    '''
    return Rs + cir_RQ(w, R=R1, Q=Q1, n=n1, fs=fs1) + elem_Q(w,Q,n)

def cir_RsRQRQ(w, Rs, R='none', Q='none', n='none', fs='none', R2='none', Q2='none', n2='none', fs2='none'):
    '''
    Simulation Function: -Rs-RQ-RQ-
    Return the impedance of an Rs-RQ circuit. See details for RQ under cir_RQ_fit()
    
    Kristian B. Knudsen (kknu@berkeley.edu || kristianbknudsen@gmail.com)
    
    Inputs
    ----------
    w = Angular frequency [1/s]
    Rs = Series Resistance [Ohm]
    
    R = Resistance [Ohm]
    Q = Constant phase element [s^n/ohm]
    n = Constant phase element exponent [-]
    fs = Summit frequency of RQ circuit [Hz]
    R2 = Resistance [Ohm]
    Q2 = Constant phase element [s^n/ohm]
    n2 = Constant phase element exponent [-]
    fs2 = Summit frequency of RQ circuit [Hz]
    '''
    if R == 'none':
        R = (1/(Q*(2*np.pi*fs)**n))
    elif Q == 'none':
        Q = (1/(R*(2*np.pi*fs)**n))
    elif n == 'none':
        n = np.log(Q*R)/np.log(1/(2*np.pi*fs))

    if R2 == 'none':
        R2 = (1/(Q2*(2*np.pi*fs2)**n2))
    elif Q2 == 'none':
        Q2 = (1/(R2*(2*np.pi*fs2)**n2))
    elif n2 == 'none':
        n2 = np.log(Q2*R2)/np.log(1/(2*np.pi*fs2))
        
    return Rs + (R/(1+R*Q*(w*1j)**n)) + (R2/(1+R2*Q2*(w*1j)**n2))

def cir_RsRQRQ2(w, Rs, R='none', Q='none', n='none', fs='none', R2='none', Q2='none', n2='none', fs2='none'):
    '''
    Simulation Function: -Rs-RQ-Q-
    
    Inputs
    ----------
    w = Angular frequency [1/s]
    Rs = Series Resistance [ohm]
    
    R1 = Resistance in (RQ) circuit [ohm]
    Q1 = Constant phase element in (RQ) circuit [s^n/ohm]
    n1 = Constant phase elelment exponent in (RQ) circuit [-]
    fs1 = Summit frequency of RQ circuit [Hz]
    Q = Constant phase element of series Q [s^n/ohm]
    n = Constant phase elelment exponent of series Q [-]
    '''
    return Rs + cir_RQ(w, R=R, Q=Q, n=n, fs=fs) + cir_RQ(w, R=R2, Q=Q2, n=n2, fs=fs2)

def cir_RsRQRQQ(w, Rs,Q, n, R1='none', Q1='none', n1='none', fs1='none', R2='none', Q2='none', n2='none', fs2='none'):
    return Rs + cir_RQ(w, R=R1, Q=Q1, n=n1, fs=fs1) + cir_RQ(w, R=R2, Q=Q2, n=n2, fs=fs2) + elem_Q(w,Q,n)

#OUTDATED FUNCTION
def full_graphing(path, lst = None):
    bad_mpts = []
    if not lst:
        path_files = [f for f in listdir(path) if isfile(join(path, f)) if f[-3:] == 'mpt']
        for i in path_files:
            try:
                print(i, ' was a permissible file')
                ex_mpt = mpt_data(path,[i])
                masked_mpt = mpt_data(path,[i], mask = ex_mpt.masker())
                masked_mpt.set_new_gph_dims(30,30)
                masked_mpt.mpt_plot()
                plt.show()
            except ValueError:
                bad_mpts.append(i)
                print(i, ' was a bad file, could not find a mask')
        if bad_mpts:
            print(bad_mpts, " are a list of bad mpts. You may want to take a closer look at them")
    if type(lst) == list:
        for i in lst:
            try:
                print(i, ' was a permissible file')
                ex_mpt = mpt_data(path,[i])
                masked_mpt = mpt_data(path,[i], mask = ex_mpt.masker())
                masked_mpt.set_new_gph_dims(30,30)
                masked_mpt.mpt_plot()
            except ValueError:
                bad_mpts.append(i)
                print(i, ' was a bad file, could not find a mask')
            if bad_mpts:
                print(bad_mpts, " are a list of bad mpts. You may want to take a closer look at them")
                
#OUTDATED FUNCTION
def the_ringer(path, single_file):
        print('WHOLE THING')
        ex_mpt = mpt_data(path,[single_file])
        ex_mpt.mpt_plot()
        
        print('FAST MASK')
        print(ex_mpt.fast_mask())
        fast_masked_mpt = mpt_data(path, [single_file], mask = ex_mpt.fast_mask())
        fast_masked_mpt.mpt_plot()
        
        print('MASKER0')
        print(ex_mpt.masker0())
        masker0_mpt = mpt_data(path, [single_file], mask = ex_mpt.masker0())
        masker0_mpt.mpt_plot()
        
        print('MASKER')
        print(ex_mpt.masker())
        masker_mpt = mpt_data(path, [single_file], mask = ex_mpt.masker())
        masker_mpt.mpt_plot()
                       
#PATH takes in a string that leads to the files
#CSV_CONTAINER takes an additional path that leads to a separate folder which will contain all the fitted coefficients
#if you want to just fit a single mpt or a list of mpts, you can use LST for specific fittings
#TAKE_CSV for when you want to export a csv
"""
def auto_fit(path, entry, csv_container = None):
    bad_mpts = []
    fitteds = []
    if type(entry) == list:
        for i in entry:
            try:
                #print(i, ' was a permissible file')
                ex_mpt = mpt_data(path,[i])
                out_name = 'fitted_' + ex_mpt.data[0][:-4]
                masked_mpt = mpt_data(path,[i], mask = ex_mpt.masker())
                fitteds.append(masked_mpt.guesser(csv_container = csv_container))
            except ValueError:
                ex_mpt = mpt_data(path,[i])
                out_name = 'fitted_' + ex_mpt.data[0][:-4]
                bad_mpts.append(i)
                ex_mpt.mpt_plot()
                print(i, ' was a bad file, could not find a mask')
            except TypeError:
                ex_mpt = mpt_data(path,[i])
                out_name = 'fitted_' + ex_mpt.data[0][:-4]
                ex_mpt.guesser(csv_container = csv_container)
                print(i, ' was fittable, but could not obtain a mask')
    
    if type(entry) == str:
        path_files = [f for f in listdir(path) if isfile(join(path, f)) if f[-3:] == 'mpt']
        for i in path_files:
            try:
                #print(i, ' was a permissible file')
                ex_mpt = mpt_data(path,[i])
                out_name = 'fitted_' + ex_mpt.data[0][:-4]
                masked_mpt = mpt_data(path,[i], mask = ex_mpt.masker())
                fitteds.append(masked_mpt.guesser(csv_container = csv_container))
            except ValueError:
                ex_mpt = mpt_data(path,[i])
                out_name = 'fitted_' + ex_mpt.data[0][:-4]
                bad_mpts.append(i)
                ex_mpt.mpt_plot()
                print(i, ' was a bad file, could not find a mask')
            except TypeError:
                ex_mpt = mpt_data(path,[i])
                out_name = 'fitted_' + ex_mpt.data[0][:-4]
                ex_mpt.guesser(csv_container = csv_container)
                print(i, ' was fittable, but could not obtain a mask')
    
    to_export = pd.concat(fitteds)
    return to_export
"""
#OUTDATED FUNCTION
def path_listing(path):
    path_files = [f for f in listdir(path) if isfile(join(path, f)) if f[-3:] == "mpt"]
    for i in path_files:
        print(i)