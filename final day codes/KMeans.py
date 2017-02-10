import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np 
from sklearn.cluster import KMeans

X = np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
## uncomment to see original points
# plt.scatter(X[:,0], X[:,1], s = 100)
# plt.show()


## increase number of clusters to see the effect
clf = KMeans(n_clusters = 2)
clf.fit(X)

centroids = clf.cluster_centers_

labels = clf.labels_

colors = ["g.", "r.", "c.", "b.", "k.", "g.", "g."]

for i in range(len(X)):
	plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 25)
plt.scatter(centroids[:,0], centroids[:,1], marker = 'x', s = 150, linewidths = 5)
plt.show()
