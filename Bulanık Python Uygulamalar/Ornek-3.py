# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:54:17 2022

@author: karaci
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import skfuzzy.membership as mf

sicaklik=ctrl.Antecedent(np.arange(20,81,1), 'Sıcaklık')
sicaklik_degisim=ctrl.Antecedent(np.arange(0,6,0.1), 'Sıcaklık Değişimi')
motor_hizi=ctrl.Consequent(np.arange(100,1001,1), 'Motor Hızı')

sicaklik['Low']=mf.trapmf(sicaklik.universe,[20,25,35,40])
sicaklik['Med']=mf.trapmf(sicaklik.universe,[30,42,55,80])
sicaklik.view()



sicaklik_degisim['Low']=fuzz.trapmf(sicaklik_degisim.universe,[0,0.3,1,2])
sicaklik_degisim['Med']=fuzz.trapmf(sicaklik_degisim.universe,[0.5,1.3,2,3])
sicaklik_degisim['Hig']=fuzz.trapmf(sicaklik_degisim.universe,[1,3,4,5])
sicaklik_degisim.view()

motor_hizi['Slow']=fuzz.trapmf(motor_hizi.universe,[100,250,350,500])
motor_hizi['Med']=fuzz.trapmf(motor_hizi.universe,[300,400,500,700])
motor_hizi['Fast']=fuzz.trapmf(motor_hizi.universe,[500,650,750,1000])
motor_hizi.view()

#motor_hizi.defuzzify_method='som'
#motor_hizi.defuzzify_method='lom'
motor_hizi.defuzzify_method='mom'
#motor_hizi.defuzzify_method='centroid'

ctrl.Rule(and_func=fmax)

rule1=ctrl.Rule(sicaklik['Low'] & sicaklik_degisim['Low'],motor_hizi['Fast'])
rule2=ctrl.Rule(sicaklik['Med'] & sicaklik_degisim['Med'],motor_hizi['Slow'])
rule3=ctrl.Rule(sicaklik['Low'] & sicaklik_degisim['Med'],motor_hizi['Fast'])
rule4=ctrl.Rule(sicaklik['Med'] & sicaklik_degisim['Low'],motor_hizi['Med'])


motor_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4])
motoring=ctrl.ControlSystemSimulation(motor_ctrl)
motoring.input['Sıcaklık']=35
motoring.input['Sıcaklık Değişimi']=1

print("Üyelik Sıcaklık Low=",fuzz.interp_membership(sicaklik.universe,sicaklik['Low'].mf,35))
print("Üyelik Sıcaklık Med=",fuzz.interp_membership(sicaklik.universe,sicaklik['Med'].mf,35))

print("Üyelik Sıcaklık Değişimi Low=",fuzz.interp_membership(sicaklik_degisim.universe,sicaklik_degisim['Low'].mf,1))
print("Üyelik Sıcaklık Değişimi Med=",fuzz.interp_membership(sicaklik_degisim.universe,sicaklik_degisim['Med'].mf,1))
print("Üyelik Sıcaklık Değişimi Hig=",fuzz.interp_membership(sicaklik_degisim.universe,sicaklik_degisim['Hig'].mf,1))



motoring.compute()
print ("Motor Hızı=",motoring.output['Motor Hızı'])


motor_hizi.view(sim=motoring)