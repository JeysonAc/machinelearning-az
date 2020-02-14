# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:02:16 2020

@author: Jeyson
"""

#Plantilla de preprocesado - Datos faltantes

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv("..\datasets\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values


#Tratamiento de nulos
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])


#Tratamiento de nulos
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])