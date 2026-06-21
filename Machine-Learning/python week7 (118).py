# SVM---Handling high dimentional Data


# =====================================================================
# SVM---Impact of High-Dimensional Spaces (Ziada Features Ka Asar)
# =====================================================================

# 1. High-dimensional data (e.g., text, genes) leads to the curse of dimensionality
# Asan Matlab: Jab data me columns (features) boht ziada ho jayein (jaise text ya DNA data), 
# toh computer ke liye patterns dhoondna boht mushkil ho jata hai, jise 'Curse of Dimensionality'
#  mean(kab dimension bht zada hojae) kehte hain.


# 2. Distances between data points become less meaningful, increasing overfitting risk
# Asan Matlab: Ziada dimensions me points ka aapas ka fasla ajeeb ho jata hai aur samajh nahi aata, 
# jiski wajah se model pure data ko ratta maar leta hai (Overfitting) aur naye data par fail ho jata hai.


# 3. Kernel computations become more complex & expensive
# Asan Matlab: Ziada features hone ki wajah se math calculations boht lambi aur complex ho jati hain, 
# jisse computer ka boht ziada dimaag (CPU/RAM) aur time kharch hota hai.


# 4. SVM can still find a separating hyperplane, but support vectors are critical for stability
# Asan Matlab: In sab mushkilat ke baajood SVM itna zoorawar hai ke woh wahan bhi boundary line dhoond leta hai, 
# lekin us boundary ko sahi jagah tika kar rakhne ke liye 'Support Vectors' boht zaroori hote hain.


# =====================================================================
# SVM---Regularization Techniques (C Parameter Ka Asal Maqsad)
# =====================================================================

# 1. Regularization controls overfitting by penalizing model complexity
# Asan Matlab: Regularization ek aisa break ya control hai jo model ko data 
# ratta maarne (Overfitting) se rokta hai aur usay simple rakhta hai.


# 2. Small C allows misclassifications, resulting in a smoother boundary & better generalization
# Asan Matlab: Jab hum 'C' ki value choti (e.g., C=0.1) rakhte hain, toh model naram ustaad ban jata hai. 
# Woh thodi boht ghalatiyan (misclassifications) maaf kar deta hai, jisse boundary smooth banti hai aur model 
# naye data par sahi chalta hai.


# 3. Large C reduces misclassifications, leading to a tighter fit with risk of overfitting
# Asan Matlab: Jab hum 'C' ki value badi (e.g., C=10 ya 100) rakhte hain, toh model boht sakht ban jata hai. 
# Woh ek bhi ghalati bardasht nahi karta aur boundary ko ajeeb tareeqe se kheenchta hai, jisse 'Overfitting'
#  (ratta maarne) ka khatra barh jata hai.


# 4. Combine with kernel selection & cross-validation to tune C
# Asan Matlab: Best result ke liye hum sahi Kernel aur sahi 'C' value ko 
# 'Cross-Validation' (data ko badal badal kar test karne wali technique) ke sath mila kar dhoondte hain.


# 2. Key Concept: What is Tuning?
# Asan Matlab: Tuning ka matlab hai hit-and-trial khatam karna. Computer khud boht saari C values (0.1, 1, 10) 
# aur alag-alag kernels (linear, rbf) ko aapas me test karta hai aur jo combination sabse best accuracy de, 
# usay select kar leta hai.


# =====================================================================
# SVM---Handling High Dimensions (Ziada Features Ka Ilaaj)
# =====================================================================

# 1. Feature Selection Methods: Select the most relevant features by analyzing variance & correlation
# Asan Matlab: Agar aapke paas 100 columns hain, to unme se faltu columns mita do. 
# Sirf woh columns (features) rakho jo sabse zaroori hain aur jinme asli information hai.


# 2. Dimensionality Reduction: Use Principal Component Analysis (PCA) to reduce feature dimensions
# Asan Matlab: Yeh ek jadoo ki machine hai jise PCA kehte hain. Yeh 100 mushkil columns ko aapas me nichor kar 
# unka asar sirf 2 ya 3 naye columns me badal deti hai, taake computer asani se boundary line bana sake.



# coding:


import numpy as np
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest,f_classif
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# create high-dimentisonal dataset(100 features)

x,y=make_classification(
    n_samples=1000,
    n_features=100,          #very high dimention
    n_informative=10,       #only 10 truly usefulll features
    n_redundant=40,
    n_repeated=10,
    random_state=42
)


x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.2,random_state=42
)

print("original feature dimension:",x.shape[1])



# baseline SVM(risk of overfitting)

svm_baseline=SVC(kernel="rbf",C=10)   #weak regularization
svm_baseline.fit(x_train,y_train)
pred_base=svm_baseline.predict(x_test)
acc_base=accuracy_score(y_test,pred_base)
print(acc_base)



# regularized SVM(stronger regularization)
svm_baseline=SVC(kernel="rbf",C=1)   #strong regularization
svm_baseline.fit(x_train,y_train)
pred_base=svm_baseline.predict(x_test)
acc_base1=accuracy_score(y_test,pred_base)
print(acc_base1)



# dimentionality reduction:PCA

pca=PCA(n_components=20)    #reduce 100--->20 dimensions
x_train_pca=pca.fit_transform(x_train)
x_test_pca=pca.transform(x_test)

svm_pca=SVC(kernel="rbf",C=1)
svm_pca.fit(x_train_pca,y_train)
pred_pca=svm_pca.predict(x_test_pca)
acc_pca=accuracy_score(y_test,pred_pca)
print(acc_pca)




# feature selection:select top 20 feature
selector=SelectKBest(score_func=f_classif,k=20)
x_train_sel=pca.fit_transform(x_train,y_train)
x_test_sel=pca.transform(x_test)

svm_sel=SVC(kernel="rbf",C=1)
svm_sel.fit(x_train_sel,y_train)
pred_sel=svm_sel.predict(x_test_sel)
acc_sel=accuracy_score(y_test,pred_sel)





# results for class discussion
print("performance comparison: ")

print(f"baseline svm (high c):   {acc_base:.3f}")
print(f"regularized svm (lower c):   {acc_base1:.3f}")
print(f"svm+pca(20 components):   {acc_pca:.3f}")
print(f"svm+feature selection(20):   {acc_sel:.3f}")




print("explained varaince by pca (first 20 componenets)",
          np.sum(pca.explained_variance_ratio_))