#Importar dataset
#dataset = read.csv("..\datasets\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Data.csv")
dataset = read.csv("Data.csv")
dataset = dataset[,2:3]


##Dividir en entrenamiento y Test

#install.packages("caTools")
library(caTools)

set.seed(123)
split = sample.split(dataset$Purchased,SplitRatio = 0.8)
training_set = subset(dataset,split==TRUE)
testing_set = subset(dataset,split==FALSE)


#Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

