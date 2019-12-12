import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)
centers = [ [1,1], [-1,-1], [1,-1] ]
iris = datasets.load_iris()
X = iris.data #x coordinates
y = iris.target #y coordinates

#we're making an array in which we init 3 kmeans cluster algos
#First make 3 clusters
#Second make 8 clusters
#Third is to make 3 clusters with a lot of data from mean distance (from center)
#Last is to create a random cluster
estimators = {'k_means_iris_3':KMeans(n_clusters=3),
            'k_means_iris_8':KMeans(n_clusters=8),
            'k_means_iris_bad_init':KMeans(n_clusters=3, n_init=1,
            init='random')}

fignum = 1
for name, est in estimators.items():
    fig = plt.figure(fignum, figsize=(4,3)) #Creating a fiture of size 4x3
    plt.clf() #clear the current figure
    ax = Axes3D(fig, rect=[0,0,.95,1], elev=48, azim=134) #simply creating a rectangle
    plt.cla() #clear the current axis
    est.fit(X) #setting x values in output plot
    labels = est.labels_

    ax.scatter(X[:,3], X[:,0], X[:,2], c=labels.astype(np.float)) #make our values scatter X[:,3] => values until 3
    ax.w_xaxis.set_ticklabels([]) #set text values for tick labels
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Petal width') #set the label for the x axis
    ax.set_ylabel('Sepal length') #set the label for the y axis
    ax.set_zlabel('Petal length') #set the label for the z axis
    fignum = fignum + 1

#plot the x & y axis without any clustering of data
fig = plt.figure(fignum, figsize=(4,2))
plt.clf() #clear the current figure
ax = Axes3D(fig, rect=[0,0, .95, 1], elev=48, azim=134) #setting next figure
plt.cla() #clear the current axis

for name, label in [
    ('Setosa', 0),
    ('Versicolour', 1),
    ('Virginica', 2)]:
    #setting labels
    ax.text3D(X[y == label,3].mean(),
        X[y == label, 0].mean() + 1.5,
        X[y == label, 2].mean(),name,
        horizontalalignment='center',
        bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
#reorder the labels to have colors matching the cluster results
y = np.choose(y,[1,2,0]).astype(np.float) #simple color matching
ax.scatter(X[:,3], X[:,0], X[:,2], c=y)

#Here is another plot
ax.w_xaxis.set_ticklabels([]) #set text values for tick labels
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Petal width') #set the label for the x axis
ax.set_ylabel('Sepal length') #set the label for the y axis
ax.set_zlabel('Petal length') #set the label for the z axis
plt.savefig('plot.png')
print('Plot saved to `plot.png`. Open it from Projects Pane to see the graph.')
