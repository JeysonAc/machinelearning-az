#Importar dataset
#dataset = read.csv("..\datasets\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv")
dataset = read.csv("Data.csv")

#Plantilla de preprocesado - Datos faltantes

#Tratamiento de nulos
dataset$Age = ifelse(is.na(dataset$Age)
                     ,ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE))
                     ,dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary)
                        ,ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE))
                        ,dataset$Salary)