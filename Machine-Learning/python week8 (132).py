# k-means clustering--implementaion with sickit-learn---part2


# k-means clustering: unsupervised method to group similar data points
# minimize intra-cluster  varince (inertia)
# choosing k requires metrics (elbow,silhoutee house) and domain knwoldege
# pyhton implementaion is starightfowrad with sickit learn

# 1.import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score



# 2 laod dataset

wine=load_wine()
x=wine.data
feature_names=wine.feature_names


# convert to dataframe
df=pd.DataFrame(x,columns=feature_names)

print("dataset shape:",df.shape)
print("first 5 rows")
print(df.head())

# 3 select two feature for visualization

# since we are not using pca,we select two features for  direct 2D visualization

selected_feature=['alcohol','malic_acid']
x_selected=df[selected_feature].values

print("selected features:",selected_feature)


# 4. feature engineering 
# important because k-means use distance calculation

scaler=StandardScaler()
x_scaled=scaler.fit_transform(x_selected)

print("feature scaling  completed")


# 5 finding optimal number of clusters (Elbow method)

inertia_values=[]
k_range=range(1,11)

for k in k_range:
    kmeans=KMeans(n_clusters=k,random_state=42,n_init=10)
    kmeans.fit(x_scaled)
    inertia_values.append(kmeans.inertia_)


# plot elbow curve
plt.figure()
plt.plot(k_range,inertia_values,marker='o')
plt.title("elbow method for optimal k")
plt.xlabel("number of cluster k")
plt.ylabel("inertia")
plt.show()


# k-means clustering--implementaion with sickit-learn
# 6 train k-mean model
# assume optimal cluster =3 from elbow method
kmeans=KMeans(n_clusters=3,random_state=42,n_init=10)
cluster=kmeans.fit_predict(x_scaled)

# add cluster labels
df['cluster']=cluster

print("cluster centers (scaled values):")

print(kmeans.cluster_centers_)


# 7.visualizing clusters
plt.figure()

plt.scatter(
    x_scaled[:,0],
    x_scaled[:,1],
    c=cluster
)

# plot centrioids
plt.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    marker='X',
    s=200
)
plt.title("k-mean clustering (Alcohol vs Malic Acid)")
plt.xlabel("alcohol (scaled)")
plt.ylabel("malic acid (scaled)")
plt.show()

# evaluating clustering performance
# internal evaluation metric
sil_score=silhouette_score(x_scaled,cluster)

print("silluette score is :",sil_score)

# cluster distribution

print(" \n number of sample in each cluster")
print(df['cluster'].value_counts())