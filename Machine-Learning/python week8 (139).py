# PCA-- Eigenvectors and Eigen Values
# eigen vectors:A vector whose direction does not change under a linear transformation
# eigen value:scalar including how much the eigen vector is stretched during transformation


# formula:AV=λV
# A=covariance matrix
# v=eigenvector
# λ=eigenvalue

# role in PCA:
# compute covraince matrix of the data
# eigenvectors of covraince matrix:
# directions of principal components
# principal component show the trend of data
# eigenvalues:amount of varince capture by each principal component

# example:3D dataset:top2 eigenvectors with largest eigenvalues capture most variance

# Advantages of using Eigenvectors and Eigen Values:
# allows identification of important direction(principal compoennt in Data)
# help educe dimentionality while preserving varinace
# provides mathemattical foundation for PCA

# consideration:
# requires stanndarization of feature for meaningful eigenvectors
# (mean=0,variance=1).
# eigenvectors or orthogonal-->ensure principal components are uncorrelated
# eigenvalues sum up to total varince in the dataset


# ==================================================================================
# PCA: EIGENVECTORS & EIGENVALUES (COMPLETE STEP-BY-STEP NOTE)
# ==================================================================================

# ----------------------------------------------------------------------------------
# POINT 1: Eigenvectors Definition
# "eigen vectors: A vector whose direction does not change under a linear transformation"
# ----------------------------------------------------------------------------------
# EXPLANATION: 
# Jab hum data par koi math ka operation chalate hain (linear transformation), toh 
# saare points aur arrows apni jagah badal lete hain. Lekin data ke andar kuch 
# jadooi arrows (vectors) aise hote hain jinka RUKH (Direction) bilkul nahi badalta—
# woh bilkul seedhe apni purani line par hi rehte hain. Un raston ko Eigenvectors kehte hain.


# ----------------------------------------------------------------------------------
# POINT 2: Eigenvalues Definition
# "eigen value: scalar including how much the eigen vector is stretched during transformation"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Jab data transform hota hai, toh woh jadooi rasta (eigenvector) apni jagah par 
# rehte hue ya toh lamba khinch jata hai ya chota ho jata hai. Woh rasta kitna 
# khinchta (`stretched`) hai, us khinchne ke NUMBER ya score ko Eigenvalue kehte hain.


# ----------------------------------------------------------------------------------
# POINT 3: Mathematical Formula
# "formula: AV = λV (A=covariance matrix, v=eigenvector, λ=eigenvalue)"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - A (Covariance Matrix): Yeh hamare saare purane columns ke aapas ke rishton ka naksha hai.
# - V (Eigenvector): Woh naye raste hain jo hum dhoond rahe hain.
# - λ (Lambda / Eigenvalue): Us raste ki apni taqaat ya score hai.
# - ASLI MATLAB: Jab hum data ke nakshe (A) ko kisi raste (V) se multiply karte hain, 
#   toh rasta badalta nahi hai, bas apni taqaat (λ) ke mutabiq lamba (λV) ho jata hai.


# ----------------------------------------------------------------------------------
# POINT 4: Role in PCA
# "role in PCA: compute covariance matrix of the data"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# PCA shuru hote ہی computer sabse pehle poore data ka 'Covariance Matrix' nikaalta 
# hai taake usay pata chal sake ke kaun sa column kis column ke sath kitna juda hua hai.


# ----------------------------------------------------------------------------------
# POINT 5: Directions of Principal Components
# "eigenvectors of covariance matrix: directions of principal components"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Jo eigenvectors is matrix se nikalte hain, asal me wahi hamare naye "Principal 
# Components (PCs)" ke raste hote hain. Yeh computer ko batate hain ke naye axes 
# kis angle par banayen.


# ----------------------------------------------------------------------------------
# POINT 6: Trend of Data
# "principal component show the trend of data"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yeh naye principal components (raste) data ka asli rukh ya pattern (trend) dikhate 
# hain ke data asal me kis taraf bhaag raha hai.


# ----------------------------------------------------------------------------------
# POINT 7: Variance Capture
# "eigenvalues: amount of variance capture by each principal component"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Har naye raste (PC) ke paas apni ek Eigenvalue hoti hai. Yeh value batati hai ke 
# us raste ne pure data ki kitni maloomat ya bikhrao (variance) apne andar sameta hai. 
# Badi eigenvalue matlab zyada maloomat.


# ----------------------------------------------------------------------------------
# POINT 8: 3D Dataset Example
# "example: 3D dataset: top2 eigenvectors with largest eigenvalues capture most variance"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Agar hamare paas 3 columns (3D data) hain, toh computer 3 raste nikaalega. Hum 
# unme se sabse badi Eigenvalues wale top 2 raste rakh lenge aur teesre ko chodh denge. 
# Is tarah 3D data aasan ho kar 2D ban jayega aur maloomat bhi zaya nahi hogi.


# ----------------------------------------------------------------------------------
# POINT 9: Advantages
# "Advantages: allows identification of important direction, help reduce dimensionality 
# while preserving variance, provides mathematical foundation for PCA"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Isse data ke sabse zaroori rukh (important directions) ka pata chal jata hai.
# - Columns kam ho jaate hain par data ki asli jaan (variance) bach jati hai.
# - Yeh pure PCA ko ek pakki mathematical buniyaad deta hai, koi tuka nahi hota.


# ----------------------------------------------------------------------------------
# POINT 10: Considerations & Rules
# "consideration: requires standardization of feature (mean=0, variance=1), 
# eigenvectors are orthogonal, eigenvalues sum up to total variance"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Standardization (StandardScaler) zaroori hai, warna bade numbers wale columns 
#   eigenvectors ko apni taraf khinch lenge aur result ghalat aayega.
# - Saare eigenvectors 'Orthogonal' (90-degree) hote hain, yaani naye columns ke 
#   beech me koi milawat ya correlation nahi hoti.
# - Agar aap saari eigenvalues ko aapas me jama (sum) kar dein, toh woh pure data ke 
#   kul bikhrao (Total Variance) ke barabar hota hai.
# ==================================================================================



# coding:

import numpy as np
#  sample dataset (2 features):

x=np.array([
    [2,3],
    [3,5],
    [4,2],
    [5,6],
    [6,5]
    
])

# step1   mean center the data
x_centered=x-np.mean(x,axis=0)
print(x_centered)


# step2:computer covariance matrix
cov_matrix=np.cov(x_centered,rowvar=False)
print("covariance matrix:",cov_matrix)


# step3: compue eigenvalue and eigen vectors
eigenvalues,eigenvectors=np.linalg.eig(cov_matrix)
print("eigen value is :",eigenvalues)


# step4:sort eigenvalues in descending order
idx=np.argsort(eigenvalues)[::-1]
eigenvalues=eigenvalues[idx]

eigenvectors=eigenvectors[:,idx]
print("eigenvectors (principal componenets):",eigenvectors)




# step5:explained variance ratio: 
explained_variance_ratio=eigenvalues/np.sum(eigenvalues)
print("explained variance ratio:",explained_variance_ratio)



