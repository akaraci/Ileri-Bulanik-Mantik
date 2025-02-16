# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:22:13 2023

@author: akara
"""

from simpful import *
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
DS1 = FuzzySet(points=[[0, 1.],  [10, 0.]], term="Soguk")
DS2 = FuzzySet(points=[[5, 0.], [20, 1.], [35, 0.]], term="Iliman")
DS3 = FuzzySet(points=[[25, 0.],  [40, 1.]], term="Sicak")
FS.add_linguistic_variable("Outside_Temperature", LinguisticVariable([DS1, DS2, DS3], concept="Dış Sıcaklık"))
#FS.plot_variable("Outside_Temperature")


IS1 = FuzzySet(points=[[0, 1.],  [12, 0.]], term="Soguk")
IS2 = FuzzySet(points=[[10, 0.], [25, 1.], [40, 0.]], term="Normal")
IS3 = FuzzySet(points=[[30, 0.],  [45, 1.]], term="Sicak")
FS.add_linguistic_variable("Inside_Temperature", LinguisticVariable([IS1, IS2, IS3], concept="İç Sıcaklık"))
#FS.plot_variable("Inside_Temperature")


FS.plot_variable("Outside_Temperature",element=32.)
FS.plot_variable("Inside_Temperature",element=12.)

# Define output crisp values
FS.set_crisp_output_value("Dusuk", 10.)
FS.set_crisp_output_value("Orta", 30.)
FS.set_output_function("Yuksek", "0.8 * Outside_Temperature - 0.5 * Inside_Temperature + 20")

#

# print("\n--------------------------------------------")
# print("Service->poor member degree:",S_1.get_value(6.5))
# print("Service->good member degree:",S_2.get_value(6.5))
# print("Service->excellent member degree:",S_3.get_value(6.5))
# print("\n--------------------------------------------")
# print("Food->rancid member degree:",F_1.get_value(9.8))
# print("Food->delicious member degree:",F_2.get_value(9.8))


# Define fuzzy rules
R1 = "IF (Outside_Temperature IS Soguk) AND (Inside_Temperature IS Soguk) THEN (Heating_Power IS Yuksek)"  #0.0199 üyelik derecesi gelir, k=5
R2 = "IF (Outside_Temperature IS Iliman) AND (Inside_Temperature IS Normal) THEN (Heating_Power IS Orta)"
R3 = "IF (Outside_Temperature IS Sicak) AND (Inside_Temperature IS Sicak) THEN (Heating_Power IS Dusuk)"
FS.add_rules([R1, R2, R3])

# Set antecedents values
FS.set_variable("Outside_Temperature",40.)
FS.set_variable("Inside_Temperature", 35.)
result=FS.Sugeno_inference(["Heating_Power"])
#0.0199*5+0.7*15+0.98*21.3/(0.0199+0.7+0.98)
#(0.0995+10.5+20.874)/1.699=31.4735/1.699=18.524
# Perform Sugeno inference and print output
print(FS.Sugeno_inference(["Heating_Power"]))

