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
shape = data.shape
print(shape)

print("\nThere are 150 rows and 5 columns")
print("\nData type for each attribute")
types = data.dtypes
print(types)

print("\nDescriptive Statistics")
#how much data to show. Width applies to width of our console
pandas.set_option('display.width', 100)
#The data values must not be greater than 3 digits, e.g. 3.054. If we have precision of 5, then we'd get 3.05400.
pandas.set_option('precision', 3)
description = data.describe()
print(description)

print("\nCorrelation Between Attributes")
#Shows relations of values to one another. 0 == no relation, -1 == negatively related, 1 == postively related
correlations = data.corr(method='pearson')
print(correlations)

print("\nSkew For Data")
skew = data.skew()
print(skew)