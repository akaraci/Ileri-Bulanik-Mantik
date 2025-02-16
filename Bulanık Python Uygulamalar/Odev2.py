# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:04:41 2022

@author: karaci
"""

import numpy as np
import matplotlib.pyplot as plt
mesafe=np.arange(-500,500,0.1) 
uyelik=np.array([])
z=[]

for x in mesafe:
    if (x<200):uyelik=np.append(uyelik, 1)
    elif x>=200 and x<=500: uyelik=np.append(uyelik,(500-x)/300)
    else: uyelik=np.append(uyelik, 0)

plt.plot(mesafe,uyelik,'b:')
plt.title("Yakın Bulanık Kümesi")
plt.xlabel("Mesafe")
plt.ylabel("Üyelik Derecesi")