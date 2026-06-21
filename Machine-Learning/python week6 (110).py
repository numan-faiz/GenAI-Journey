# random forest --how it works part1
# bootstraping explained--->
# Bootstrapping Random Forest ka sab se pehla aur aasan step hai jiska matlab hai "Data ki duplicate nakal"
# " (copy) banana".Bootstrapping Kia Hai?Asan Matlab: Apne asal data (Dataset) mein se random tareeqe se
# rows chunna, jahan ek hi row baar-baar bhi select ho sakti hai (Sampling with replacement).Fayda: Is se
# har Tree ko ek alag aur thoda badla hua  data milta hai.

# Sampling with replacement ka asan matlab hai: "Data uthao, note karo, aur wapis usi dabbe mein daal do."

# randomly sample n data points with replacement for each tree
# some sample appear multiple times,while others are not selected (out-of-bag samples)

# example of boostaping:
# A data set of 10-> tree1 may see[2,5,3,3,7..], while tree 2 may see[1,4,2,2,5..]

# benefits of boostraping-->
# diffrent subsample of the dataset are used for each decision tree
# each decison tree learns in a diffrent way
# improved decison making
# better classifire than a single decison tree
# widely used for improved results


# out-of-bag (oob) sample-->
# usage--> used as an internal testing dataset and a good candidate for model evaluation
# oob wo hta ju data select na hva hu dataset me  phr usko hm testing ke liye rakh skty oky 



# benefit:provide an efficient performance estimate,especially for small datasets



# bagging(bootstap agrregation):
# combine predictions from multiple trees to reduce variance
# classification-->majority voting is used
# regression-->average of predictions is taken


# Bagging ka matlab hai: Alag-alag Decision Trees ka mashwara mila kar final prediction karna.
# Yeh 3 steps mein kaam karta hai:Bootstrap (Data Copy): Asal data se random tareeqe se rows chun kar har 
# Tree ke liye alag dataset banaya jata hai. Is mein ek hi row baar-baar bhi aa sakti hai (Sampling with 
# replacement).Train (Trees Banana): Har dataset par ek alag Decision Tree parallel (ek sath) train
# hota hai. Har Tree alag data ki wajah se mukhtalif cheez seekhta hai.Aggregating (Result Milana): 
# Naye data ki prediction ke liye saare Trees apna jawab dete hain:Classification (Yes/No): Jis jawab
# ko sab se zyada votes milen (Majority Voting), woh final jawab hota hai.Regression (Numbers): Saare
# Trees ke answers ka Average nikal kar final jawab banta hai.Maqsad: Overfitting (ratta marna) ko
# khatam karna aur model ki accuracy badhana.

# example of bagging-->
# 5 trees[setosa,setosa,virginica,setosa,versicolo]
# majority vote=setosa

# benefits of bootstap aggregation:
# preserve low bias while improving model stability



# coding--->
# random forest

import numpy as np
import sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


sklearn.set_config(print_changed_only=False) # <--- YEH LINE KAM KAREGI!


# load dataset
data=load_iris()
x=data.data
y=data.target
feature_names=data.feature_names
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=42
)

# train random forest(bootstraping+many trees)
rf=RandomForestClassifier(
    n_estimators=500,   # number of trees in the forest
    random_state=42,    
    max_depth=None,     # allow fulll trees
    bootstrap=True,     # sampling with replacement (bootstraping)
    n_jobs=-1
)
print(rf.fit(x_train,y_train))

# make prediction (majority voting)

y_pred=rf.predict(x_test)
print(y_pred)



# evaluate performance

print("random forest performance")
print(f"accuracy:{accuracy_score(y_test,y_pred):3f}")