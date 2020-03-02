
#---------------------------------Regresión Linean Múltiple--------------------------------

#Cargar Dataset
dataset = read.csv("50_Startups.csv")
#dataset = dataset[,1:3]


#Codificar variables categóricas
dataset$State = factor(dataset$State
                         ,levels = c("New York","California","Florida")
                         ,labels = c(1,2,3))

#Dividir Dataset en Entrenamiento y Pruebas
#install.packages("caTools")
library(caTools) 
set.seed(123) 
split = sample.split(dataset$Profit,SplitRatio = 0.8)
training_set = subset(dataset,split==TRUE)
testing_set = subset(dataset,split==FALSE)

#Ajustar el modelo de regresión lineal múltiple con el conjunto de Entrenamiento
regression = lm(formula = Profit ~ .,
                data = training_set)

# Predicción de los resultados del conjunto de prueba
y_pred = predict(regression,newdata = testing_set)


summary(regression)
