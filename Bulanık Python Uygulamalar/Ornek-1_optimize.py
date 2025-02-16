# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:28:13 2022

@author: karaci
"""

import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

def bulanik_kume_ciz(where,whichvar,whichset,label,renk,title):
    where.plot(whichvar,whichset,renk,linewidth=2, label=label)
    where.set_title(title)
    where.legend()

def yatay_dikey_cizgi_ciz(where,Xdikey,ydikey,Xyatay,yyatay):
    where.plot(Xdikey,ydikey,'r',linewidth=1, linestyle='--')
    where.plot(Xyatay,yyatay,'r',linewidth=1, linestyle='--')
    

#----------------------Değişkenler oluşturuluyor----------------------
var_model=np.arange(2002,2013,1)
var_km=np.arange(0,100001,1)
var_fiyat=np.arange(0,40001,1)
#-----------------------------------------------------------------------
fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(nrows=5,figsize=(15,20))

#----Model için Üyelik Fonksiyonları Tanımlanıyor
set_model_dusuk=mf.trimf(var_model, [2002,2002,2007])
set_model_orta=mf.trimf(var_model, [2002,2007,2012])
set_model_yuksek=mf.trimf(var_model, [2007, 2012, 2012])
#----Model için Bulanık Kümeler Çizdiriliyor
bulanik_kume_ciz(ax0,var_model,set_model_dusuk,"Düşük",'r',"Model")
bulanik_kume_ciz(ax0,var_model,set_model_orta,"Orta",'g',"Model")
bulanik_kume_ciz(ax0,var_model,set_model_yuksek,"Yüksek",'b',"Model")


#----Kilometre için Üyelik Fonksiyonları Tanımlanıyor
set_km_dusuk=mf.trimf(var_km, [0,0,50000])
set_km_orta=mf.trimf(var_km, [0,50000,100000])
set_km_yuksek=mf.trimf(var_km, [50000, 100000, 100000])
#----Kilometre için Bulanık Kümeler Çizdiriliyor
bulanik_kume_ciz(ax1,var_km,set_km_dusuk,"Düşük",'r',"Kilometre")
bulanik_kume_ciz(ax1,var_km,set_km_orta,"Orta",'g',"Kilometre")
bulanik_kume_ciz(ax1,var_km,set_km_yuksek,"Yüksek",'b',"Kilometre")


#----Fiyat için Üyelik Fonksiyonları Tanımlanıyor
set_fiyat_dusuk=mf.trimf(var_fiyat, [0,0,20000])
set_fiyat_orta=mf.trimf(var_fiyat, [0,20000,40000])
set_fiyat_yuksek=mf.trimf(var_fiyat, [20000, 40000, 40000])
#----Fiyat için Bulanık Kümeler Çizdiriliyor
bulanik_kume_ciz(ax2,var_fiyat,set_fiyat_dusuk,"Düşük",'r',"Fiyat")
bulanik_kume_ciz(ax2,var_fiyat,set_fiyat_orta,"Orta",'g',"Fiyat")
bulanik_kume_ciz(ax2,var_fiyat,set_fiyat_yuksek,"Yüksek",'b',"Fiyat")
#----------------------------------------------------------------------------------------------

#Hesaplama Yapılacak Girişler belirleniyor
input_model=2011
input_km=25000

#----------Herbir Girişin giriş bulanık kümelerine üyelik dereceleri hesaplanıyor
model_fit_dusuk=fuzz.interp_membership(var_model,set_model_dusuk,input_model)
model_fit_orta=fuzz.interp_membership(var_model,set_model_orta,input_model)
model_fit_yuksek=fuzz.interp_membership(var_model,set_model_yuksek,input_model)

#Üyelik dereceleri grafik üzerinde gösteriliyor
#         [x1,x2],[y1,y2] şeklinde düz çizgi verileri verilmelidir.
#çağrılan fonkdiyon prototipi: yatay_dikey_cizgi_ciz(where,Xdikey,ydikey,Xyatay,yyatay)
yatay_dikey_cizgi_ciz(ax0, [input_model,input_model],[0,model_fit_dusuk], [2002,input_model],[model_fit_dusuk,model_fit_dusuk])
yatay_dikey_cizgi_ciz(ax0, [input_model,input_model],[0,model_fit_orta], [2002,input_model],[model_fit_orta,model_fit_orta])
yatay_dikey_cizgi_ciz(ax0, [input_model,input_model], [0,model_fit_yuksek], [2002,input_model], [model_fit_yuksek,model_fit_yuksek])


km_fit_dusuk=fuzz.interp_membership(var_km,set_km_dusuk,input_km)
km_fit_orta=fuzz.interp_membership(var_km,set_km_orta,input_km)
km_fit_yuksek=fuzz.interp_membership(var_km,set_km_yuksek,input_km)
yatay_dikey_cizgi_ciz(ax1, [input_km,input_km],[0,km_fit_dusuk], [0,input_km],[km_fit_dusuk,km_fit_dusuk])
yatay_dikey_cizgi_ciz(ax2, [input_km,input_km],[0,km_fit_orta], [0,input_km],[km_fit_orta,km_fit_orta])
yatay_dikey_cizgi_ciz(ax3, [input_km,input_km],[0,km_fit_yuksek],[0,input_km],[km_fit_yuksek,km_fit_yuksek])
#------------------------------------------------------------------------------------------------

#Kurallar oluşturuluyor ve uygulanıyor Mamdani, Min kuralına göre çıkışa uygulanıyor. Kesme yapılıyor
rule1 = np.fmin(np.fmin(model_fit_dusuk, km_fit_yuksek), set_fiyat_dusuk)
rule2 = np.fmin(np.fmin(model_fit_orta, km_fit_orta), set_fiyat_orta)
rule3 = np.fmin(np.fmin(model_fit_yuksek, km_fit_dusuk), set_fiyat_yuksek)
#max-çarpım için aşağıdaki kurallar kullanılabilir.
# rule1 = (np.fmin(model_fit_dusuk, km_fit_yuksek)* set_fiyat_dusuk)
# rule2 = (np.fmin(model_fit_orta, km_fit_orta)* set_fiyat_orta)
# rule3 = (np.fmin(model_fit_yuksek, km_fit_dusuk)* set_fiyat_yuksek)

#Herbir kuraldan elde edilen çıkış değişkenine ait bulanık kümeler çizidiriliyor
bulanik_kume_ciz(ax3,var_fiyat,rule1,"Rule1",'r',"Her bir kuraldan elde edilen çıkış kümeleri")
bulanik_kume_ciz(ax3,var_fiyat,rule2,"Rule2",'g',"Her bir kuraldan elde edilen çıkış kümeleri")
bulanik_kume_ciz(ax3,var_fiyat,rule3,"Rule3",'b',"Her bir kuraldan elde edilen çıkış kümeleri")
#-----------------------------------------------------------------------------------------------------

#Her bir kuraldan elde edilen Çıkışların Maksimumu Alınarak birleştirme (aggretitaion) yapılıyor
out1=np.fmax(rule1,rule2)
out_set_final=np.fmax(out1,rule3) #Nihai bulanık çıkış kümemiz
ax4.fill_between(var_fiyat,out_set_final, 'b', linestyle=':', linewidth=2, label='out')
ax4.set_title("Çıkış-Bulanık Küme Birleşimi")
#---------------------------------------------------------------------------------------------------
#Durulama İşlemi Yapılıyor
#Durulama Yöntemleri
# 'centroid' — Centroid of the area under the output fuzzy set
# 'bisector' — Bisector of the area under the output fuzzy set
# 'mom' — Mean of the values for which the output fuzzy set is maximum
# 'lom' — Largest value for which the output fuzzy set is maximum
# 'som' — Smallest value for which the output fuzzy set is maximum

defuzzified_centroid = fuzz.defuzz(var_fiyat, out_set_final, 'centroid') 
print("Fiyat(centroid)=",defuzzified_centroid)

defuzzified_bisector = fuzz.defuzz(var_fiyat, out_set_final, 'bisector') 
print("Fiyat(bisector)=",defuzzified_bisector)

defuzzified_mom = fuzz.defuzz(var_fiyat, out_set_final, 'mom') 
print("Fiyat(mom)=",defuzzified_mom)

defuzzified_lom = fuzz.defuzz(var_fiyat, out_set_final, 'lom') 
print("Fiyat(lom)=",defuzzified_lom)

defuzzified_som = fuzz.defuzz(var_fiyat, out_set_final, 'som') 
print("Fiyat(som)=",defuzzified_som)

hangisi=defuzzified_centroid
result = fuzz.interp_membership(var_fiyat, out_set_final, hangisi)
ax4.plot([0,hangisi],[result,result],'r')
ax4.plot([hangisi,hangisi],[0,result],'r')


