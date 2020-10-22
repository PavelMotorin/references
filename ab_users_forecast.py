import os
import pandas as pd
import numpy as np
from scipy.stats import norm, zscore
def print_mean_forecast(mean, std, delta = [0.9, 0.91, 0.92, .93, .94, .95, .96, .97, .98, .99], metric='ARPU'):
    res = pd.DataFrame(index=delta, columns=['res'])
    for d in delta:
        _res = int(sample_size_mean_difftest(mean - mean*d,  std)//1000) # thousands of players
        print (metric + ': '+str(d)+" "+str(_res))
        res['res'][d] = _res
    return res
def print_diff_forecast(prob, delta = [0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99], metric='Conv'):
    res = pd.DataFrame(index=delta, columns=['res'])
    for d in delta:
        _res = int(sample_size_perc_difftest(prob, (prob * d)))
        print (metric + ': '+str(d)+" "+str(_res))
        res['res'][d] = _res
    return res
def sample_size_mean_difftest(d, s, power=0.8, sig=0.05):
    z = norm.isf([sig/2]) 
    zp = -1 * norm.isf([power])
    n = (2*(s**2)) * ((zp + z)**2) / (d**2)
    return (n[0])
def sample_size_perc_difftest(p1, p2, power=0.8, sig=0.05):
    z_power = -1 * norm.isf([power])
    z_sig = norm.isf([sig/2]) 
    d1 = p1 * (1 - p1)
    d2 = p2 * (1 - p2)
    n = (d1 + d2) * ((z_power + z_sig)**2) / ((p1 - p2)**2)
    return n.round()[0]
def print_mean_forecast_eazy(mean, std, delta = [0.8, 0.9], metric='attempts'):
    res = pd.DataFrame(index=delta, columns=['res'])
    for d in delta:
        _res = int(sample_size_mean_difftest(mean - mean*d,  std)) # thousands of players
        print (metric + ': '+str(d)+" "+str(_res))
        res['res'][d] = _res
    return res
