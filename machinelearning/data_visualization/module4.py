import pandas
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

print("\nView first 30 rows of pima-indians-diabetes.data")
url = "https://skillstackcdn.s3.amazonaws.com/mldata/pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)

data.plot(kind='box', subplots='True', layout=(3,3),sharex=False,sharey=False)
data.hist()
plt.savefig('plot.png')
scatter_matrix(data)
plt.savefig('scatter.png')
print('Plots saved to `plot.png` and `scatter.png`. Open it from Projects Pane to see the graphs.')
