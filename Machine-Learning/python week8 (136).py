# hierarchical clustering---implementation with scikit learn part1
# fiiting agglomarative clustering model
# affinity=distance metric (eucleadean)
# linkage=method between compute distance between clusters (wrad,complete,avergae)


# ==================================================================================
# FITTING AGGLOMERATIVE CLUSTERING (ROMAN URDU - EXTREME SHORT)
# ==================================================================================

# 1. Model Fitting:
#    Python me hum 'AgglomerativeClustering' class ka use karke model ko data fit karte hain.

# 2. Affinity (Ab iska naya naam 'metric' hai):
#    Iska matlab hai "Points ke beech ka fasla naapne ka scale". 
#    Jaise hum maps par 'Euclidean distance' (seedha line ka fasla) use karte hain.

# 3. Linkage:
#    Iska matlab hai "Do pure groups ke beech me fasla compute karne ka tareeqa".
#    - ward: Groups ko aise jorhta hai ke bikhrao (variance) kam se kam barhe (Best).
#    - complete: Do groups ke sabse door wale points ka fasla dekhta hai.
#    - average: Saare points ka aapas me average fasla nikaalta hai.
# ==================================================================================


# hierarchical clusterig with scikit learn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

# 1--load datset(real dataset,no syntehtic)

data=load_iris()
x=pd.DataFrame(data.data,columns=data.feature_names)

print("dataset shape:",x.shape)
print("first 5 rows:",x.head())


# 2. fit hierarchical (agglomarative) lustering
hc=AgglomerativeClustering(
    n_clusters=3,    # number of clusters to extarct
    linkage="ward"   # minmize within cluster vraince
)
cluster_label=hc.fit_predict(x)

# 3. Attach cluster labels to dataset

x["cluster"]=cluster_label
print("cluster count")
print(x["cluster"].value_counts())


print("sample with cluster lables:")
print(x.head()) 