# k-NN--performance optimization techniques


# =====================================================================
# KNN---Choosing K Value (Short & Simple Notes)
# =====================================================================

# 1. Small k (Chota k) -> Sensitive to Noise | May OVERFIT
#    Matlab: Har choti baat par jaldi yakeen karna aur dhoka kha jana.

# 2. Large k (Bada k)  -> Smooth Boundary  | May UNDERFIT
#    Matlab: Boht zyada aalsi ho jana aur data ki barikiyaan chodh dena.

# 3. Rule of Thumb     -> k = √n (Square root of total training samples)
#    Matlab: Agar 100 samples hain, toh k = 10 se shuru karein.

# 4. Best Method       -> Cross-Validation
#    Matlab: Computer khud saare numbers test karke sabse best k chunega.


# challenge for K-NN formance:
# huge dataset make issue challenge so distance calculation bht zyada mushkil hoajege or time b lagega

# solutions:
# PCA--->dimensionality reduction---reduce number of feature


# tips:
# apply feature normalization
# perform dimentionality reduction
# select optimal k for best performance

# coding-->
# optimizing k-NN performance:k selection,normalization,PCA
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score



# 1---Load dataset(Moderately high-dimensional)
data=load_breast_cancer()
x,y=data.data,data.target
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42,stratify=y
)
print("original dimension",x_train.shape)


# 2---normalize features (very important for k-NN)
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)


# choose optimal k(simple search)

best_k=None
best_acc=0


for k in range(1,21):
    knn=KNeighborsClassifier(n_neighbors=k,metric="euclidean")
    knn.fit(x_train_scaled,y_train)
    y_pred=knn.predict(x_test_scaled)
    acc=accuracy_score(y_test,y_pred)
    print(f"with k: {k},accuracy: {acc:.4f}")

    if acc>best_acc:
        best_acc=acc
        best_k=k

print(f"best k found: {best_k} with accuracy:{best_acc:.4f}")



# dimensionality reduction with PCA

pca=PCA(n_components=10)   #reduce dimensions
x_train_pca=pca.fit_transform(x_train_scaled)
x_test_pca=pca.transform(x_test_scaled)


print("Reduced dimensions: ",x_train_pca.shape)


# Train k-nn after pca using the best k
knn_pca=KNeighborsClassifier(n_neighbors=best_k)
knn_pca.fit(x_train_pca,y_train)


y_pred_pca=knn_pca.predict(x_test_pca)
acc_pca=accuracy_score(y_test,y_pred_pca)


print(f"accuracy after PCA: {acc_pca:.4f}")
print("explained variance by 10 components",
          round(np.sum(pca.explained_variance_ratio_),3))