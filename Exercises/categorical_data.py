# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:01:39 2020

@author: Jeyson
"""
#Plantilla de preprocesado - Datos categóricos

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

#Codificar datos categóricos
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
labelencoder_X.fit_transform(X[:,0])
X[:,0] = labelencoder_X.fit_transform(X[:,0])


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)