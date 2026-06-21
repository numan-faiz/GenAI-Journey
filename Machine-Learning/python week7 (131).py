# k-means clustering--implementaion with sickit-learn---part1

# k--means clustering using scikit learn (basic demo)

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd


# 1  load dataset
iris=load_iris()
x=iris.data              #use features only(no label in clustering so we discard it)
print("dataset shape:",x.shape)

print(x)


# fit k-means mdoel

kmeans=KMeans(n_clusters=3,random_state=42,n_init=10,init='k-means++')
kmeans.fit(x)



# results
print("cluster centers \n",kmeans.cluster_centers_)
print("first 10 cluster lables:",kmeans.labels_[:10])