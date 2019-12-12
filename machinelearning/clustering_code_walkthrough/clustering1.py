import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

#sudo pip install --upgrade matplotlib

X = np.array([
        [1,2],
        [5,8],
        [1.5,1.8],
        [8,8],
        [1, 0.6],
        [9,11]
    ])

#we're initializing keamsn to be the KMeans algorithm (flat clustering) with the required paramter of how many clusters.
#
kmeans = KMeans(n_clusters=2)
#fit() to fit the data (i.e.,learning)
kmeans.fit(X)
#we're grabbing the varlues found for the centroids based on the fitment (data) as well as the labels for each centroid
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels) #showing assigned by Kmean algo

#Now we're going to plot and visualize the machine's findings based on our data and the fitment according to the number of clusters we've instructed it to find
colors = ["r.", "g.", "y.", "c."]

for i in range(len(X)):
    print("coordinate: ", X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

plt.scatter(centroids[:,0], centroids[:,1], marker="x", s=150, linewidths=5, zorder=10)
plt.savefig('plot.png')
print('Plot saved to `plot.png`. Open it from Projects Pane to see the graph.')