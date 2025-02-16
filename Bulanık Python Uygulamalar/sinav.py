# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:54:17 2022

@author: karaci
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import skfuzzy.membership as mf

X=ctrl.Antecedent(np.arange(6,19,1), 'X')
Y=ctrl.Antecedent(np.arange(3,12,1), 'Y')
Z=ctrl.Consequent(np.arange(-0.1,0.11,0.01), 'Z')

X['Dx']=mf.trimf(X.universe,[6,6,12])
X['Nx']=mf.trimf(X.universe,[6,12,18])
X['Yx']=mf.trimf(X.universe,[12,18,18])
X.view()

Y['Dy']=mf.trimf(Y.universe,[3,3,7])
Y['Ny']=mf.trimf(Y.universe,[3,7,11])
Y['Yy']=mf.trimf(Y.universe,[7,11,11])
Y.view()

Z['AZ1']=mf.trimf(Z.universe,[-0.1,-0.05,0])
Z['AZ2']=mf.trimf(Z.universe,[-0.1,-0.1,-0.05])
Z['DY']=mf.trimf(Z.universe,[-0.05,0,0.05])
Z['AR1']=mf.trimf(Z.universe,[0.0,0.05,0.1])
Z['AR2']=mf.trimf(Z.universe,[0.05, 0.1,0.1])
Z.view()

#motor_hizi.defuzzify_method='som'
#motor_hizi.defuzzify_method='lom'
Z.defuzzify_method='mom'
#motor_hizi.defuzzify_method='centroid'

rule1=ctrl.Rule(X['Yx'] & Y['Dy'],Z['AR1'])
rule2=ctrl.Rule(X['Yx'] & Y['Ny'],Z['AR1'])
rule3=ctrl.Rule(X['Yx'] & Y['Yy'],Z['AR2'])

rule4=ctrl.Rule(X['Nx'] & Y['Dy'],Z['AZ1'])
rule5=ctrl.Rule(X['Nx'] & Y['Ny'],Z['DY'])
rule6=ctrl.Rule(X['Nx'] & Y['Yy'],Z['AR1'])


rule7=ctrl.Rule(X['Dx'] & Y['Dy'],Z['AZ2'])
rule8=ctrl.Rule(X['Dx'] & Y['Ny'],Z['AZ1'])
rule9=ctrl.Rule(X['Dx'] & Y['Yy'],Z['AZ1'])



Z_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8])
motoring=ctrl.ControlSystemSimulation(Z_ctrl)
motoring.input['X']=10
motoring.input['Y']=10

print("X (Dx)=",fuzz.interp_membership(X.universe,X['Dx'].mf,10))
print("X (Nx)=",fuzz.interp_membership(X.universe,X['Nx'].mf,10))
print("X (Yx)=",fuzz.interp_membership(X.universe,X['Yx'].mf,10))


print("Y (Dy)=",fuzz.interp_membership(Y.universe,Y['Dy'].mf,10))
print("Y (Ny)=",fuzz.interp_membership(Y.universe,Y['Ny'].mf,10))
print("Y (Yy)=",fuzz.interp_membership(Y.universe,Y['Yy'].mf,10))


motoring.compute()
print ("Z=",motoring.output['Z'])
Z.view(sim=motoring)


