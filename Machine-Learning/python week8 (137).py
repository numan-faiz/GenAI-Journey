# hierarchical clustering---implementation with scikit learn part2

# hierachical clustering groups points into nested clusters
# agglomarative=bootoom-up
# divisive=top down
# dendogram help visualize and choose the number of clusters
# flexible with distance metrics and linkage methods
# scikit learn provide implementation and visualization tools


# coding
# hierarchical clustering: dendrogram+cluster visualization
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage,dendrogram


# hierarchical clustering---implementation with scikit learn
# 1-laod a real dataset (not blobs,not iri)
data=load_wine()
x=data.data
# standaruized features (important for distance-based methods)
x_scaled=StandardScaler().fit_transform(x)
print(x_scaled)

# 2--compute linkage matrix for dendogram
z=linkage(x_scaled,method="ward")
plt.figure(figsize=(10,6))
dendrogram(z)
plt.title("hierarchical clustering dendrogram (wine dataset)")
plt.xlabel("samples")
plt.ylabel("merge distance")
plt.tight_layout()
plt.show()

# 3.fit hierarchical clustering model
n_cluster=3     #chosen based on dendogram inspection
hc=AgglomerativeClustering(
    n_clusters=n_cluster,
    linkage="ward"
)

labels=hc.fit_predict(x_scaled)
print(labels)

# 4--reduce to 2D for visualization of clusters
pca=PCA(n_components=2,random_state=42)
x_2d=pca.fit_transform(x_scaled)


plt.figure(figsize=(6,5))

plt.scatter(x_2d[:,0],x_2d[:,1],c=labels,cmap="tab10",s=30)
plt.title("hierachical clustering result (PCA VIEW)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
plt.show()

print("cluster counts:",np.bincount(labels))