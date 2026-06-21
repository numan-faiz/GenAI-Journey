# Hierrarchical clustering----Agglomerative vs divisive methods

# Agglomerative clustering (bottom up):
# each data point starts as its own cluster
# iteratively merge the two closest clusters based on a chosen distance metric
# repeat merging until all points are combined into a single cluster


# linkage options:single linakeh:distnace between closest points
# complete linkage:distance between farthest points
# average linkage:average distance between all points

# divisive clustering:
# all data points starts in one large cluster
# iteratively split clusters into smaller clusters based on dissimilarity
# splitting continues until each point is its own cluster or stopping criterion is met

# less common than agglomarative due to computationl complexity
# comprison:
# agglomarative:simpler ,widely used easier to implement

# divisive can capture global structure better,more computationally expensivechoice 
# depend on datset size and analysis goal

# ==================================================================================
# AGGLOMERATIVE VS DIVISIVE & LINKAGES: EXTREME SHORT NICHOR
# ==================================================================================

# 1. Agglomerative Clustering (Bottom-Up / Neeche se Upar):
#    - Shuruat: Har ek point apna alag akela group (cluster) hota hai.
#    - Kaam: Computer do sabse kareeb wale groups ko aapas me jorhta (merge) jata hai.
#    - Khatam: Yeh tab tak chalta hai jab tak saare points jorh kar aik bada group na ban jayein.


# 2. Linkage Options (Do groups ke beech fasla naapne ke 3 tareeqe):
#    - Single Linkage: Dono groups ke sabse KAREER wale points ka fasla naapna.
#    - Complete Linkage: Dono groups ke sabse DOOR wale points ka fasla naapna.
#    - Average Linkage: Dono groups ke SAARE points ka aapas me average fasla naapna.


# 3. Divisive Clustering (Top-Down / Upar se Neeche):
#    - Shuruat: Saare points pehle se aik hi bade group ke andar hote hain.
#    - Kaam: Computer dushmani (dissimilarity) ke hisab se is bade group ko torta (split) jata hai.
#    - Khatam: Yeh tab tak chalta hai jab tak har point bilkul akela alag group na ban jaye.
#    - Note: Yeh boht bhaari (computationally expensive) hai, isliye log isay kam use karte hain.


# 4. Asli Muqabla (Comparison):
#    - Agglomerative: Aasan hai, dunya me sabse zyada yahi use hota hai.
#    - Divisive: Mushkil aur mehanga hai, par yeh pure data ka global structure (bada nakshe ka view) zyada accha samajhta hai.
# ==================================================================================


# agglomarative vs divisive  clustering
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering,BisectingKMeans


# 1--/laod dataset
x,_=make_blobs(
    n_samples=200,
    random_state=42,centers=3,cluster_std=0.9
)
# 2 agglomrative (bottomup)
agg=AgglomerativeClustering(n_clusters=3,linkage="ward")    #minimer the sum of sqaure difeerences
agg_labels=agg.fit_predict(x)

# 3  divisive (top down)
# (bisecting k means is practical divisive method)
div=BisectingKMeans(n_clusters=3,random_state=42)
div_label=div.fit_predict(x)
print(div_label)



# visual comparison

fig,axes=plt.subplots(1,2,figsize=(9,4))
axes[0].scatter(x[:,0],x[:,1],c=agg_labels,cmap="tab10",s=15)
axes[0].set_title("agglomerative (bottom-up)")

axes[1].scatter(x[:,0],x[:,1],c=div_label,cmap="tab10",s=15)
axes[1].set_title("DIVISIVE (Top-Down)")


plt.tight_layout()
plt.show()