# PCA--implemetation with sickit learn part1
# PCA reduce dimentionality by proejecting data onto principal compoenets


# coding-->
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# step1--> load dataset (30 features)

data=load_breast_cancer()
x=data.data
y=data.target
print(x)


# step2 standarize feature (critical for PCA)
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
print(x_scaled)


# step3: apply pca (reduce to 2 compoennets)
pca=PCA(n_components=2)
x_pca=pca.fit_transform(x_scaled)
print(x_pca)


# step4 evaluate dimentionality reduction

print("original shape",x.shape)
print("Reduced shape",x_pca.shape)

print("explained variance ratio",pca.explained_variance_ratio_)
print("total variancce preserved",np.sum(pca.explained_variance_ratio_))



# step 5:visualize pca result
plt.figure()
plt.scatter(x_pca[:,0],x_pca[:,1],c=y)
plt.xlabel("principal component 1")
plt.ylabel("principal compoennet 2")
plt.title("PCA on Breast Cance Dataset (2 components)")
plt.tight_layout()
plt.show()