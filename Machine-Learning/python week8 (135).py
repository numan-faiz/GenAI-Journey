# hierarchical clustering---dendrograms and cluster selection

# dendorgram: 
# A dengrogram is a tree dighram representing the hierarchy of clusters
# each merge or split is represnedted by a branch connecting clusters
# hight of the branch shows distance or disimilarity between clsuters

# choosing the number of cluster:
# cut the dendogram at a specific height to define clsuters
# look for large vertical gaps between merges to decide optimal number of clusters
# can use quantitaive measures like inconsistency coefficient or silhoutte score to validate clusters


# interpreting the dendogram:
# clustres that merge at low height are more similar
# clusters that merge at high heights are more disimilar 
# helps visualize nested structure and relationship between cluster


# ==================================================================================
# DENDROGRAMS & CLUSTER SELECTION: EXTREME SHORT NICHOR
# ==================================================================================

# 1. Dendrogram Kya Hai? (What is it?)
#    - Yeh ek darakht (Tree) jaisa graph hota hai jo groups ka poora khandan dikhata hai.
#    - Jab do groups aapas me judte hain, toh wahan ek nayi shaakh (Branch) banti hai.
#    - Shaakh ki OONCHAI (Height) batati hai ke un dono groups me kitna fasla ya dushmani thi.


# 2. Clusters Ki Ginti Kaise Chunyein? (Choosing Clusters Number)
#    - Cut the Dendrogram: Hum graph par ek seedhi aari (horizontal line) chala kar darakht ko kaat dete hain.
#    - Large Vertical Gaps: Jahan sabse lambi khali khari line (vertical gap) nazar aaye, wahan se kaatna
#  sabse best hota hai.
#    - Validation: Isko pakka karne ke liye hum 'Silhouette Score' ka test bhi use kar sakte hain.


# 3. Dendrogram Ko Parhna Kaise Hai? (Interpreting the Dendrogram)
#    - Low Height Merge: Jo points bilkul neeche hi aapas me jud gaye, woh aapas me boht zyada ek jaise (Similar) hain.
#    - High Height Merge: Jo lines boht upar ja kar aapas me mili hain, un groups me boht zyada farq (Dissimilar) hai.
# ==================================================================================


# Dendrogram ek aisa naksha hai jisme jo neeche miley woh pakke dost (similar), jo upar ja kar
#  miley woh dushman (dissimilar), aur jahan sabse lambi vertical line mile, wahan se darakht 
# ko kaat kar (Cut) groups alag kar lo.


# ==================================================================================
# LINKAGE AUR 'WARD' KYA HAI? (ROMAN URDU NICHOR)
# ==================================================================================
# - Linkage: Do alag-alag groups ke beech me fasla (distance) naapne ka tareeqa hai.
# - 'Ward': Yeh sabse best linkage hai, jo do groups ko jorhte waqt yeh dekhta hai 
#   ke naye group ke andar ka bikhrao (variance) sabse kam hona chahiye taake tight groups banein.
# ==================================================================================

# dendogram visualization for hierachical clustering:
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster



# create a sample dataset
x,_=make_blobs(
    n_samples=50,
    centers=3,
    cluster_std=1.0,
    random_state=42
)


# 2-->computional hierachical linkage(agglomarative)
# 'ward' minimize within-cluster variance

z=linkage(x,method="ward")


# 3-->plot dighram

plt.figure(figsize=(12,6))
dendrogram(z)
plt.title("hierarchical clustering dendogram")
plt.xlabel("data points")
plt.ylabel("distance (merge height)")
plt.axhline(y=10,linestyle="--")   # example horizantal cut

plt.show()

# 4-- choose number of cluster form denmgoram (equavalent to cutting at a heigh)
k=3
cluster=fcluster(z,t=k,criterion="maxclust")
print("cluster assighments:",cluster)