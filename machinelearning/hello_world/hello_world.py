#Here is a little problem related to Data analysis.
#We have to analize data as we did in our previous module number 2
#You need to follow all the steps we did follow in module 2

#Peek at the Data
#Dimensions of Dataset
#Descriptive Statistics
#Correlation Between Attributes
#Skew For Data

#Our dataset link => https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
#Above is the same data we used in module 2
#This time we have to analyze the data differently

import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']
#loading data
data = pandas.read_csv(url, names=names)

#peak at unseen data
peek = data.head(30)
print("\nShowing first 30 rows of iris.data")
print(peek)

print("\nDimensions of Dataset")
print(data.shape)


print("\nDescriptive Statistics")
print(data.describe())
