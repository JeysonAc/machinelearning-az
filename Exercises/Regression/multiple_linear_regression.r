
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

#Modelo óptimo con eliminación hacia atrás
# regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, 
#                 data = dataset)
# 
# regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, 
#                 data = dataset)
# 
# regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, 
#                 data = dataset)
# 
# regression = lm(formula = Profit ~ R.D.Spend, 
#                 data = dataset)
# 
backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  return(summary(regressor))
}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)


summary(regression)
