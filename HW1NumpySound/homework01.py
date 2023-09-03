import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from IPython.display import Audio
from numpy. fft import fft, ifft
get_ipython().run_line_magic('matplotlib', 'inline')

import requests

url = "https://raw.githubusercontent.com/k5yi/econ2005/master/datasets/kid_laugh.wav"
laugh = requests.get(url).content

with open('kid_laugh.wav', 'wb') as f:
    f.write(laugh)

fs, data = read('kid_laugh.wav')

data = data[:,0]

url = "https://raw.githubusercontent.com/k5yi/econ2005/master/datasets/woosh.wav"
woosh = requests.get(url).content

with open('woosh.wav', 'wb') as f:
    f.write(woosh)
    
fs, woosh = read('woosh.wav')

woosh = woosh[:,0]

def reverse_play(sample, fs = 44100):
    return int(fs), np.flip(sample, axis=0) 

def amplify(sample_level, fs = 44100):
    return int(fs), data*10**(sample_level/20)

def echo_effect(sample, fs, delay, repeat, effect):
    data = sample
    for i in range(repeat):
        sample = np.r_[data,np.zeros((int(fs*delay)*(i+1),2))] + np.r_[np.zeros((int(fs*delay),2)),sample*(1-effect)]
    return sample

def mixing(data, weight):  
    if data[0].size < data[1].size :
        mix = (weight[0]*np.resize(data[0], data[1].shape))+(data[1]*weight[1])    
    else :
        mix = (weight[1]*np.resize(data[1], data[0].shape))+(data[0]*weight[0])
    return fs, mix



