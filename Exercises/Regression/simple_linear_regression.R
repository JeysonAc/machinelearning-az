# Regresi??n Lineal Simple

#----------PREPROCESAMIENTO DE DATOS-------------------
#Importar dataset
#dataset = read.csv("..\datasets\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv")
dataset = read.csv("Salary_Data.csv")
dataset = dataset[,1:3]


##Dividir en entrenamiento y Test

#install.packages("caTools")
library(caTools)

set.seed(123)
split = sample.split(dataset$Salary,SplitRatio = 2/3)
training_set = subset(dataset,split==TRUE)
testing_set = subset(dataset,split==FALSE)


#Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])


#----------CONSTRUCCI??N DEL MODELO -------------------

#Ajustar modelo de regresi??n lineal simple - Datos entrenamiento
regressor = lm(formula = Salary ~ YearsExperience, training_set)

#Predecir los resultados con el conjunto de test
y_pred = predict(regressor,newdata = testing_set)


#-----------VISUALIZACI??N DE RESULTADOS---------------
#install.packages("ggplot2")
library("ggplot2") 

#Visualizaci??n de conjunto de datos de entrenamiento
ggplot() +
  geom_point(aes(x=training_set$YearsExperience, y = training_set$Salary),
             colour="red") + 
  geom_line(aes(x=training_set$YearsExperience, 
                y=predict(regressor,newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo vs. A??os de experiencia (Conjunto de entrenamiento)") + 
  xlab("A??os de experiencia") + 
  ylab("Sueldo (en $)")
  

#Visualizaci??n de conjunto de datos de prueba
ggplot() +
  geom_point(aes(x=testing_set$YearsExperience, y = testing_set$Salary),
             colour="red") + 
  geom_line(aes(x=training_set$YearsExperience, 
                y=predict(regressor,newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo vs. A??os de experiencia (Conjunto de pruebas)") + 
  xlab("A??os de experiencia") + 
  ylab("Sueldo (en $)")




