# PCA - Implementation with Scikit-Learn - Part II

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# step1 laod dataset (64 features)
digits=load_digits()
x=digits.data
y=digits.target
print(x)


# step2 standarize feature
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
print(x_scaled)


# step 3 apply PCA (reduce to 2 componenents)
pca=PCA(n_components=2)
x_pca=pca.fit_transform(x_scaled)

print(x_pca)


# step4 evaluate dimensionality reduction
print("original shape",x.shape)
print("reduced shape",x_pca.shape)

print("explained  vraince ration:",pca.explained_variance_ratio_)
print("total variance preserved:",np.sum(pca.explained_variance_ratio_))


plt.figure(figsize=(10,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=y)
plt.xlabel("principal componet 1")
plt.ylabel("principal componet 2")
plt.title("PCA on digits dataset(2 componenets)")
plt.show()