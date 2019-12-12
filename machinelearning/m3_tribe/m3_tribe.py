import pandas
print("\nView first 30 rows of pima-indians-diabetes.data")
url = "https://skillstackcdn.s3.amazonaws.com/mldata/pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
peek = data.head(30)
print(peek)

print("\nshape")
shape = data.shape
print(shape)

print("\ndata types for each attribute")
types = data.dtypes
print(types)

print("\nDescriptive Statistics")
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)

print("\nCorrelation")
correlations = data.corr(method='pearson')
print(correlations)

print("\nSkew for data")
skew = data.skew()
print(skew)