# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:55:11 2020

@author: JeysonA
"""
#------------------REGRESIÓN POLINÓMICA ---------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importar Dataset
dataset = pd.read_csv("../../datasets\Part 2 - Regression\Section 6 - Polynomial Regression/Position_Salaries.csv")
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

"""
#División de datos en entrenamiento y pruebas
from sklearn.model_selection import train_test_split
x_train,y_train,x_test,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
"""


#Ajustar modelo de regresión lineal
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)

#Ajustar modelo de regresión polinómica
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)

#Visualizar resultados Modelo Lineal
"""
plt.scatter(x,y,color="red")
plt.plot(x,lin_reg.predict(x),color="blue")
plt.title("Moodelo de Regresión Lineal")
plt.xlabel("Nivel del empleado")
plt.ylabel("Sueldo")
plt.show()
"""

#Visualizar resultados Modelo Polinómico
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape(len(x_grid),1)
plt.scatter(x,y,color="red")
plt.plot(x_grid,lin_reg_2.predict(poly_reg.fit_transform(x_grid)),color="blue")
plt.title("Modelo de Regresión Polinómica")
plt.xlabel("Nivel del empleado")
plt.ylabel("Sueldo")
plt.show





