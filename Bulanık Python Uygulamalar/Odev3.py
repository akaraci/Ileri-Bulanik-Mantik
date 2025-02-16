# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 18:39:08 2022

@author: karaci
"""


import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,100,1) 

b=40   #Genişlik
c=50    #Tepe noktası
z=[]
def uyelik_hesapla(a,b,c,u):      
        if (u<a):uyelikderecesi=0
        if (u>=a and u<=b):uyelikderecesi=2*(pow(((u-a)/(c-a)),2))
        if (u>b and u<=c): uyelikderecesi=1-2*(pow(((u-c)/(c-a)),2))
        if (u>c): uyelikderecesi=1
        return uyelikderecesi        

for u in x:
    if (u<=c): z.append(uyelik_hesapla(c-b, c-b/2, c,u))
    if (u>c): z.append(1-uyelik_hesapla(c,c+b/2,c+b,u))


plt.plot(x,z)
    
    
 



