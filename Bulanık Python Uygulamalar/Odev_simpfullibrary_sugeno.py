# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:18:51 2023

@author: akara
"""

import simpful as sf

# A simple fuzzy model describing how the heating power of a gas burner depends on the oxygen supply.

FS = sf.FuzzySystem()

# Define a linguistic variable.
S_1 = sf.FuzzySet( points=[[0, 1.],  [1., 1.],  [1.5, 0]],          term="low_flow" )
S_2 = sf.FuzzySet( points=[[0.5, 0], [1.5, 1.], [2.5, 1], [3., 0]], term="medium_flow" )
S_3 = sf.FuzzySet( points=[[2., 0],  [2.5, 1.], [3., 1.]],          term="high_flow" )
FS.add_linguistic_variable("OXI", sf.LinguisticVariable( [S_1, S_2, S_3] ))

FS.plot_variable("OXI",element=.51)
print(S_1.get_term(),":",S_1.get_value(0.51)) #low_flow : 1.0
print(S_2.get_term(),":",S_2.get_value(0.51))#medium_flow : 0.01
print(S_3.get_term(),":",S_3.get_value(0.51))#high_flow : 0


# Define consequents.
FS.set_crisp_output_value("LOW_POWER", 0) 
FS.set_crisp_output_value("MEDIUM_POWER", 25) 
FS.set_output_function("HIGH_FUN", "OXI**2")

# Define fuzzy rules.
RULE1 = "IF (OXI IS low_flow) THEN (POWER IS LOW_POWER)" #Üyelik=1, k=0
RULE2 = "IF (OXI IS medium_flow) THEN (POWER IS MEDIUM_POWER)" #Üyelik=0.01, k=25
RULE3 = "IF (NOT (OXI IS low_flow)) THEN (POWER IS HIGH_FUN)" #bu kural çalışmaz
FS.add_rules([RULE1, RULE2, RULE3])
# Set antecedents values, perform Sugeno inference and print output values.
FS.set_variable("OXI", .51)
#çıkış=(0*1+0.01*25)/(1+0.01)=0.2475247

print (FS.Sugeno_inference(['POWER']))