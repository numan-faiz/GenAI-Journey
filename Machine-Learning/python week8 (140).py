# PCA--dimentionality reduction concept

# select top k principal components that capture the maximum variance
# project data onto these k components to obtained a reduced dataset
# formula for projected data=x_reduced=X*W

# w-->matrix of top k eigenvectors
# x=original standarized data


# trade-offs:
# more componenets lead to less information loss but higher dimentionlaity
# fewer commnents information loss more but a simple model and faster computation

# A scree plot can help select k by plotting eigenvalues and identifying the elbow point

# example:original data with 13 features can be reduced using pca to 3 component capturing 90% variance   
# the reduced data ca be used for clustering,visulaization or downstream machine learning tasks


# ==================================================================================
# PCA: DIMENSIONALITY REDUCTION CONCEPT (COMPLETE STEP-BY-STEP NOTE)
# ==================================================================================

# ----------------------------------------------------------------------------------
# POINT 1: Select Top K Components
# "select top k principal components that capture the maximum variance"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Jab computer saare naye raste (Principal Components) aur unka score (Eigenvalues) 
# nikaal leta hai, toh hum sabse bade score wale top "K" (K matlab koi bhi number, 
# jaise 2 ya 3) raste chun lete hain jo pure data ki sabse zyada maloomat (variance) 
# apne andar rakhte hain.


# ----------------------------------------------------------------------------------
# POINT 2: Project Data & Formula
# "project data onto these k components to obtained a reduced dataset. 
# formula for projected data: X_reduced = X * W (W=matrix of top k eigenvectors, X=original standardized data)"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - X (Original Data): Hamara asli data jo scale (standardize) hua wa hai.
# - W (Weight Matrix): Jo top K eigenvectors humne chune hain, unka table.
# - X_reduced: Chota aur naya data.
# - ASLI MATLAB: Jab hum asli data (X) ko top eigenvectors (W) ke sath multiply 
#   (Dot Product) karte hain, toh data purane nakshe se uchal kar naye chote nakshe 
#   par girta hai. Is tarah columns kam ho kar data chota (reduce) ho jata hai.


# ----------------------------------------------------------------------------------
# POINT 3: Trade-offs (Faide aur Nuqsan ka Balance)
# "more components lead to less information loss but higher dimensionality. 
# fewer components information loss more but a simple model and faster computation"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yeh ek tarazu ki tarah hai:
# - Agar zyada Components rakhoge: Maloomat ka nuqsan (Information Loss) boht kam hoga, 
#   lekin data ka size abhi bhi bada (high dimensionality) rahega.
# - Agar kam Components rakhoge: Data boht chota aur simple ho jayega, computer super-fast 
#   chalega, lekin thodi maloomat zyada zaya ho sakti hai.


# ----------------------------------------------------------------------------------
# POINT 4: Scree Plot (K Chunne Ka Tareeqa)
# "A scree plot can help select k by plotting eigenvalues and identifying the elbow point"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Scree Plot ek simple graph hota hai jahan hum x-axis par naye columns (PCs) rakhte hain 
# aur y-axis par unki taqaat (Eigenvalues). Is graph me jahan par kohni (Elbow Point) 
# banti hai, wahan se hume pata chal jata hai ke kitne "K" components rakhna sabse best hai.


# ----------------------------------------------------------------------------------
# POINT 5: Asli Misaal (Wine Dataset/13 Features Example)
# "example: original data with 13 features can be reduced using pca to 3 component 
# capturing 90% variance. the reduced data can be used for clustering, visualization..."
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Farz karein aapke data me 13 columns (features) hain. PCA un 13 columns ka juice 
# nikaal kar sirf 3 naye columns (PC1, PC2, PC3) bana dega, aur un 3 columns me pure 
# data ki 90% maloomat safe rahegi! Ab is chote data ko aap aaram se 3D graph par 
# dekh (visualize) sakte hain, ya is par K-Means clustering chalaiye, computer aik 
# jhatke me chal jayega.
# ==================================================================================


import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine

# 1load dataset (13 features--good for dimentionality reduction)
data=load_wine()
x=data.data
print(x)

# 2
# apply pca (reduce for 13D to 2D)

pca=PCA(n_components=2)
x_reduced=pca.fit_transform(x)

print("oroginal shape",x.shape)
print("reduced shape",x_reduced.shape)


# variance information:
explained_variance=pca.explained_variance_ratio_
print("explained variance ratio",explained_variance)



total_variance_preserved=np.sum(explained_variance)
print("total variance preserved",total_variance_preserved)


information_loss=1-total_variance_preserved
print("information loss",information_loss)