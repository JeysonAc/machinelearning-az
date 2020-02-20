# -*- coding: utf-8 -*-

# Regresión Lineal Simple

#Importar librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#------------------PREPROCESAMIENTO DE DATOS---------------------

#Cargar el Dataset
dataset = pd.read_csv("../../datasets/Part 2 - Regression/Section 4 - Simple Linear Regression/Salary_Data.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

#Tratamiento de nulos
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean",axis=0)
imputer = imputer.fit(x[:,:])
x[:,:] = imputer.transform(x[:,:])

#Dividir Datastet en entrebamiento y pruebas
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/3,random_state=0)

#------------------CONSTRUCCIÓN DEL MODELO---------------------

#Modelo de Regresión Lineal Simple - Datos Entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train,y_train)

#Predecir el conjunto Test
y_pred = regression.predict(x_test)

#------------------VISUALIZAR LOS RESULTADOS---------------------
#Visualizar datos de entrenamiento
plt.scatter(x_train,y_train, color="red")
plt.plot(x_train,regression.predict(x_train), color="blue")
plt.title("Sueldo vs. Años de experiencia (Conjunto de entrenamiento")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario($)")
plt.show()

#Visualizar datos de test
plt.scatter(x_test,y_test, color="red")
plt.plot(x_train,regression.predict(x_train), color="blue")
plt.title("Sueldo vs. Años de experiencia (Conjunto de prueba")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario($)")
plt.show()