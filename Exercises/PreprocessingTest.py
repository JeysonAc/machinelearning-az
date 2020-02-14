# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:24:14 2020

@author: Jeyson
"""

#1. Importar librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#2. Cargar el Dataset
datasetTest = pd.read_csv("..\datasets\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv")
X1 = datasetTest.iloc[:,:-1].values
y1 = datasetTest.iloc[:,3].values

#3. Tratar nulos
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer = imputer.fit(X1[:,1:3])
X1[:,1:3] = imputer.transform(X1[:,1:3])

#4. Codificar datos categóricos
from sklearn.preprocessing import LabelEncoder
labelEnconder_X1 = LabelEncoder()
labelEnconder_X1.fit_transform(X1[:,0])
X1[:,0] = labelEnconder_X1.fit_transform(X1[:,0])

# Variables Dummy
from sklearn.preprocessing import OneHotEncoder
oneHotEncoder = OneHotEncoder(categorical_features=[0])
X1 = oneHotEncoder.fit_transform(X1).toarray()

#5. Dividir los datos en entrenamiento y pruebas
from sklearn.model_selection import train_test_split
X1_train,X1_test,y1_train,y1_test = train_test_split(X1,y1,test_size=0.2,random_state=0)


#6.Escalar variables
from sklearn.preprocessing import StandardScaler
sc_X1 = StandardScaler()
X1_train = sc_X1.fit_transform(X1_train)
X1_test = sc_X1.fit_transform(X1_test)



