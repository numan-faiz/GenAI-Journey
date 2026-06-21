# k-means clustering---choosing the optimal number of cluster(K)

# methods of choosing k mean number of cluster
# first set with expert
2# elbow methods:
# plot total within cluster sum of squares (wcss) versus k

# look for the "elbow" point where adding more cluster dosent significantly reduced


# ==================================================================================
# ELBOW METHOD (BEST K DHUANDNE KA TAREEQA) - SHORT NICHOR
# ==================================================================================

# 1. Expert Se Poochna:
#    Manager khud bata deta hai ke kitne groups chahiye (Jaise: Small, Medium, Large -> K=3).

# 2. Elbow Method (Kohni Tareeqa):
#    Agar koi batane wala na ho, toh hum K aur WCSS (Ghar ka fasla) ka ek graph banate hain.

# 3. WCSS Kya Hai?:
#    Group ke points ka apne Center (Boss) se fasla. Groups barhenge toh fasla kam hoga.

# 4. "Elbow" Point Dhoondna:
#    Graph ki line jahan achanak mud kar Insaan ki "Kohni" (Elbow) jaisi shape banaye.

# 5. Faisla (Final Choice):
#    Jahan par kohni banti hai, wahi hamara sabse Best "K" (Number of Clusters) hota hai.
# ==================================================================================


# silhouette Score:measue how similar a point is to its own cluster versus other cluster

# slihouette coefficient:range form 1 to -1
# close to 1-->well clusterd
# close to 0-->overlapping cluster
# negative--->misclassied point

# siloute score:higher avergaesilhoutte score indicates better cluster speration



# coding
# choosing optimal k for k-means: Elbow method+silhouette score
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# create synthetic clustering data

x,_=make_blobs(
    n_samples=100,
    random_state=42,
    centers=4,
    cluster_std=1.0
)


# compute metrics for diffrenet k values
k_values=range(2,15)

wcss=[]     # with cluster sum of sqaure fior elbow
sil_score=[]   # silhoute score

for k in k_values:
    kmeans=KMeans(n_clusters=k,random_state=42,n_init=10)
    labels=kmeans.fit_predict(x)

    wcss.append(kmeans.inertia_)   # elbow metric
    sil_score.append(silhouette_score(x,labels))

print(wcss)



# plot elbow method
plt.figure(figsize=(6,4))
plt.plot(k_values,wcss,marker="o")
plt.xlabel("number of cluster (k)")
plt.ylabel("WCSS (Inertia)")
plt.title("elbow method for optimal k")
plt.grid(True)
plt.show()


# plot Silhouette score
plt.figure(figsize=(6,4))
plt.plot(k_values,sil_score,marker="o")
plt.xlabel("number of cluster (k)")
plt.ylabel("silhouette score")
plt.title("silhouette score vs k")
plt.grid(True)
plt.show()

# print best k by slihouette
best_k=k_values[np.argmax(sil_score)]
print(f"best k according to silhouette score:",{best_k})