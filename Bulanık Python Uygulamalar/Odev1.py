# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:04:41 2022

@author: karaci
"""

import numpy as np
import matplotlib.pyplot as plt
mesafe=np.arange(0,10,0.1) 
uyelik=np.array([])


for x in mesafe:
    m=1/(1+10*pow(x-5,2))
    uyelik=np.append(uyelik,m)


plt.plot(mesafe,uyelik,'g--')
plt.title("Yakın Bulanık Kümesi")
plt.xlabel("Mesafe")
plt.ylabel("Üyelik Derecesi")

# Girilen değer için üyelik derecesi hesaplamayı siz yapın!!!!!