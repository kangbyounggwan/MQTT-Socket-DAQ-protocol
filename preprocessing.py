import glob, os
from scipy.stats import skew, kurtosis
import numpy as np
import pandas as pd



def fft_t_sum(raw):
    #fft 변환
    raw_ = np.array(raw)
    fs = 8000
    optimiz = raw_ / fs
    frequency_raw = np.fft.rfft(optimiz, n=8000)
    #t_sum 변환

    t_sum_raw = pd.DataFrame({
        'Std': np.std(frequency_raw),
        'Mean':np.mean(frequency_raw),
        'Skew': skew(frequency_raw),
        'Var': np.var(frequency_raw),
        'kurt': kurtosis(frequency_raw),
        'len': len(frequency_raw),
    },index=[0])
    print(t_sum_raw)
    return t_sum_raw


