# K-means Clustering---Intra-cluster variance and inertia

# how to minimize intra cluster variance

# make objective function first
# k-means minimze the sum of sqaured distances between points and their cluster centriod

# #  k
#    Σ   Σ     ||x - μᵢ||²
#   i=1  x∈Cᵢ

# Sum of squared distances is called inertia.

# ==================================================================================
# INTRA-CLUSTER VARIANCE & INERTIA (PURE ROMAN URDU - EXTREME SHORT)
# ==================================================================================

# 1. Intra-Cluster Variance Kam Karna:
#    Ek hi group ke saare points ko apne Boss (Centroid) ke bilkul kareeb lana.

# 2. Objective Function (Asli Target):
#    Points aur Centroid ke beech ka fasla (Distance) kam se kam karna.

# 3. Formula: Σ Σ ||x - μᵢ||²
#    - x        = Data Point
#    - μᵢ (Mu)  = Group ka Centroid (Boss)
#    - Minus    = Dono ke beech ka fasla
#    - Square   = Ghalati ko bada karke dekhna
#    - Σ (Sigma)= Saare points aur saare groups ka fasla aapas me jama (add) karna.

# 4. Inertia:
#    Isi total jama kiye hue fasle (Grand Total) ko "Inertia" kehte hain.
#    K-Means ka kaam isi Inertia ko chota karna hota hai.
# ==================================================================================


# understanding inertia:
# lower inertia-->tiggher cluster,points closer to centriod
# high inertia:dispersed clusters,poor grouping

# objective function of k mean  clustering:
# reach minimum level of inertia during optimization of iteration
# k means algorithm iteratively updates centriod to reducee inertia


# convergence and limitation:

# k-means stops when inertia no longer decrease or maximum iiteration reached
# sensitive to outliers
# can skew  centriods
# may converge to local minima;repeat wi th diffrent indutriliazton for best results




# coding


# demonstration of k-mean objectives,minimizing intra-cluster variance(inertia)



import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans



#1--> Create clustering data

x,_=make_blobs(
    random_state=42,n_samples=200,centers=3,cluster_std=1.0,
)


# 2 fir k-means
k=3
kmeans=KMeans(n_clusters=k,random_state=42,n_init=10)
labels=kmeans.fit_predict(x)




# 3plot cluster and centrioids
plt.figure(figsize=(6,5))
plt.scatter(x[:,0],x[:,1],c=labels,cmap="tab10",alpha=0.7)
plt.scatter(
    kmeans.cluster_centers_[:,0],
     kmeans.cluster_centers_[:,1],
     s=200,marker="X",color="black",
     label="Centroids"


)
plt.title("K-means clustering (k=3)")
plt.legend()
plt.show()


# 4) show inertia objective value
print("inertia (sum of sqaured distances to centrioids):")
print(round(kmeans.inertia_,2))


# 5 show effect of different k on variance
for k_test in [2,3,4,5]:
    km=KMeans(n_clusters=k_test,random_state=42,n_init=10)
    km.fit(x)

    print(f"k={k_test},inertia={round(km.inertia_,2)}")