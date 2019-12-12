from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

np.set_printoptions(precision=5, suppress=True) #supressing sicentific float notation
np.random.seed(4711)

#generate two clusters: a with 100 points, b with 50
a = np.random.multivariate_normal([10,0], [[3,1], [1,4]], size=[100]) #draw random samples from a multivariate normal distribution
b = np.random.multivariate_normal([0,20], [[3,1], [1,4]], size=[50,]) #The multivariate normal, multinormal or Gassian distrubition is a generalization of the one-dimensional normal distribution to a higher dimensions
X = np.concatenate((a,b),)
print(X.shape) #150 samples with 2 dimensions

#generate the linkage matrix
plt.scatter(X[:,0], X[:,1])
plt.show()
#create dendrogram
Z = linkage(X, 'ward') #As the scipy linkage docs tell us, 'ward' is one of the methods that can be used to calculate the distance bewteen newly formed clusters. 'ward' causes linkage() to use the Ward vaiarance minimization algorithm
plt.figure(figsize=(10,5))
plt.title('Hierachical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90., #rotate the x axis labels
    leaf_font_size=8., #font size for the x axis labels
)
plt.savefig('plot.png')
print('Plot saved to `plot.png`. Open it from Projects Pane to see the graph.')