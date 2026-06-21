# Random forest--Feature importance and out-of-bag error


# feature importance-->we see that how much importanat feature in dataset
#measures each features contribution to predictive performance
# helps identify most influential and guides selection

# computed accross all tress,not just one

# application-->interpretation,simplification, and model optimization


# calculation of feature importance
# step1--> measure reduction in impurity *gini,entropy) at each split
# step2:sum reduction across all tree and normalize(0-1)
# step3:-->rank feature;higher value reduction--->more important

# formula=delta|(n)=decrease in impurity at node n;sum over nodes where feature f used



# example of feature improtance
# house prediction:
# features,[size,bedrooms,age,loaction]
# feature importance:
# size=0.55,location=0.25,bedrooms=0.15
# model relies mostly on size,moderately on location least on age


# out-of bage-errors: ju data bach jata hy usy hm testing ke liye rkhty wo oob hta hy or jab usi data par prediction kerta
# jab ghalt niklti wo oob error hta hy 
# oob error is an internal validation metric using bootstrapped samples (1/3 left out)
# ubiased estimate of model performance  without separate validation set
# efficient ,especially for small dataset
# example:1000 samples ,each tree trains on 667-->333 oob used for testing

# calculating oob error step by step:
# identify oob samples for each tree
# predict output using that tree
# aggregate predictions accross all trees,compare  with actual
# example-->1000 samples,300/333
# correct->OOB
# accuracy=90%


# coding
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
# load dataset
data=load_breast_cancer()
x=data.data
y=data.target
feature_names=data.feature_names


# train random forest with oob estimation
rf=RandomForestClassifier(
    n_estimators=100,   #number of trees
    bootstrap=True,     #enable bootstraping
    oob_score=True,      #enable oob error
    random_state=42,
    n_jobs=-1
)
rf.fit(x,y)


# 3--out of baf (oob) error
oob_accuracy=rf.oob_score_
oob_error=1-oob_accuracy

print("out of bage evaulauation")
print(f"oob accuracy:{oob_accuracy:.4f}")
print(f"opb_error:{oob_error}:.4f")
print("No separate validation set was used")
