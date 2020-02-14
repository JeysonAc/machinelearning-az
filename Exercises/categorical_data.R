#Importar dataset
#dataset = read.csv("..\datasets\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv")
dataset = read.csv("Data.csv")

#Plantilla de preprocesado - Datos categóricos

#Codificar variables categóricas
dataset$Country = factor(dataset$Country
                         ,levels = c("France","Spain","Germany")
                         ,labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased
                           ,levels = c("No","Yes")
                           ,labels = c(0,1))