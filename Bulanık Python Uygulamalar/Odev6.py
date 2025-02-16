# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 15:58:41 2022

@author: karaci
"""

import numpy as np
import matplotlib.pyplot as plt

low,med=np.array([]), np.array([])
sicaklik=np.arange(20,81,1)

def yamuk_uyelik_hesapla(a,b,c,d):
    uyelik=[]
    for u in sicaklik:
        if (u<a):uyelik.append(0)
        elif (u>=a and u<b): uyelik.append((u-a)/(b-a))
        elif(u>=b and u<=c):uyelik.append(1)
        elif (u>c and u<=d): uyelik.append((d-u)/(d-c))
        else: uyelik.append(0)
    return uyelik
plt.rcParams["figure.figsize"] = (20,15)
def bulanık_küme_ciz(rownum,colnum,which,title):
    #Bulanık Kümler Çiziliyor
    plt.subplot(rownum,colnum,which)
    plt.subplots_adjust(hspace=0.2)
    plt.plot(sicaklik,m_low, label='LOW')
    plt.plot(sicaklik,m_med,label='MED')
    plt.xticks(np.arange(min(sicaklik),81,1))
    plt.yticks(np.arange(0,1.1,0.1))
    plt.title(title)
    plt.legend()
    
            
m_low=np.array(yamuk_uyelik_hesapla(20, 25, 35, 40))
#m_low=m_low*0.7      
m_med=np.array(yamuk_uyelik_hesapla(30, 42, 55, 80))   
#m_med=m_med*0.7      

#mamdani Kuralı Uygulanıyor ve Grafikler Çizidiriliyor
bulanık_küme_ciz(2,1,1,"Mamdani")
mamdani_kural1_cikis=np.minimum(0.40,m_low)
mamdani_kural2_cikis=np.minimum(0.75,m_med)
result=np.maximum(mamdani_kural1_cikis,mamdani_kural2_cikis)
plt.plot(sicaklik,result, linewidth=1, linestyle=':', color='b')
plt.plot(sicaklik,mamdani_kural1_cikis, linewidth=6, linestyle=':', color='b')
plt.plot(sicaklik,mamdani_kural2_cikis, linewidth=6, linestyle=':', color='r')
plt.fill_between(sicaklik,  result, facecolor='g', alpha = 1)


#--larsen çaprım kuralı uygulanıp grafik üzerine yansıtılıyor
bulanık_küme_ciz(2,1,2,"Larsen")
larsen_kural1_cikis=(0.4*m_low)
larsen_kural2_cikis=(0.75*m_med)
result=np.maximum(larsen_kural1_cikis,larsen_kural2_cikis)
plt.plot(sicaklik,result, linewidth=1, linestyle=':', color='r')
plt.plot(sicaklik,larsen_kural1_cikis, linewidth=6, linestyle=':', color='r')
plt.plot(sicaklik,larsen_kural2_cikis, linewidth=6, linestyle=':', color='r')
plt.fill_between(sicaklik,  result, facecolor='b', alpha = 1)








