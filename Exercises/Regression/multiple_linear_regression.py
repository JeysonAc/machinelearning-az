#Regresión Lineal Múltiple

#Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Dataset
dataset = pd.read_csv("../../datasets/Part 2 - Regression/Section 5 - Multiple Linear Regression/50_Startups.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

#Manejo de variables categóricas
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:,3] = labelencoder_x.fit_transform(x[:,3]) 
onehotencoder = OneHotEncoder(categorical_features=[3])
x = onehotencoder.fit_transform(x).toarray()

#Evitar trampa de variables fictisias 
x = x[:,1:]

#Divisón del Dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)


#------------------CONSTRUCCIÓN DEL MODELO---------------------

#Ajustar el modelo con el conjunto de entrenamiento All-In
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train,y_train)

#Predicción de resultados en test
y_pred = regression.predict(x_test)

#Ajustar el modelo óptimo con la Eliminación Hacias Atrás
import statsmodels.api as sm
x = np.append(arr = np.ones((50,1)).astype(int),values = x, axis = 1)
x_opt = x[:,[0,1,2,3,4,5]]
sl = 0.05


"""
x_opt = x[:,[0,1,2,3,4,5]]
regression_ols = sm.OLS(endog=y,exog=x_opt).fit()
regression_ols.summary()

x_opt = x[:,[0,1,3,4,5]]
regression_ols = sm.OLS(endog=y,exog=x_opt).fit()
regression_ols.summary()

x_opt = x[:,[0,3,4,5]]
regression_ols = sm.OLS(endog=y,exog=x_opt).fit()
regression_ols.summary()

x_opt = x[:,[0,3,5]]
regression_ols = sm.OLS(endog=y,exog=x_opt).fit()
regression_ols.summary()

x_opt = x[:,[0,3]]
regression_ols = sm.OLS(endog=y,exog=x_opt).fit()
regression_ols.summary()
"""


def backwardElimination(x,sl):
    numVars=len(x[0])
    for i in range(0,numVars):
        regressor_ols = sm.OLS(y,x.tolist()).fit()
        maxVar = max(regressor_ols.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0,numVars-i):
                if(regressor_ols.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x,j,1)
                    
    regressor_ols.summary()
    return x


x_modeled = backwardElimination(x_opt,sl)