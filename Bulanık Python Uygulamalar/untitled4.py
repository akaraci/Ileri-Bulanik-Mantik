# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:00:09 2023

@author: akara
"""

import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

var_sicaklik=np.arange(-10,10,0.1)
set_sicaklik_low=mf.gaussmf(var_sicaklik, 0, 1)
fig,(ax0)=plt.subplots(nrows=1,figsize=(15,20))
ax0.plot(var_sicaklik,set_sicaklik_low,'r',linewidth=2, label='Low')