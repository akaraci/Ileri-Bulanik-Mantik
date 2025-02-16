# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:31:49 2022

@author: karaci
"""
#%%
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#%%
#-----------Değişkenler ve Evrensel kümeler tanımlanıyor
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')
#%%
#Otomatik üyelik fonksiyonları oluşturuluyor. İtsenirse 5 ya da 7 küme de olutşrulabilir
quality.automf(3)
service.automf(3)
#quality.view()
#quality['poor'].view()
#service.view()

#Bahşiş için üyelik fonksiyonları manuel oluşturuluyor
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])
tip.view()

#%%
rule1 = ctrl.Rule(quality['good'] | service['good'], tip['high'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['poor'] & quality['poor'], tip['low'])

#%%
#-----Kontrol sistemi oluşturuluyor
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

#%%Simlation
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['quality'] = 1
tipping.input['service'] = 1
tipping.compute()
print ("",tipping.output['tip'])
tip.view(sim=tipping)




























