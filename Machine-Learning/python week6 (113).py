#  Random Forest - Hyperparameter Tuning & Optimization
# parameter tunning--->
# parameter tunning ju hy model hud select kerke karta hy 
# goal:improve predictive performance and generalization
# random forest hyperparameter control tree grwoth and ensemble behaviour
# proper tunning balance bias and variance to prevent over/underfiiting


# parameters-->max-depth,n_estimators,min_samples-split,
# min_samples_leaf,max_features

# number of trees(n_estimator):
# define the number of decison trees in the forest
# too few trees==>high variance
# more trees-->more stable predictions

# usually start fom 100 to 200 trees

# 2-->maximum depth of trees(max_depth):
# maximum levels in each tree;controls bias and varinace
# shallow(small trees) trees-->underfiiting
# deep(large) trees-->overfiiting
# so use normal range of trees


# example:max_depth=3 may miss patterns,max_depth=None may memorize

# best practice: use cross-validation or oob error;typical range 5-20.




# minimum sample to split a node:
# minimum samples  required a split node; control tree growth
# low value---overfitting
# high value---underfiitingexample:min_sample_split=2
# pureleaves;min_samples_split=50
# smoother output
# tip:tune based on dataset size,larger data set toolerate smaller splits


# minimum samples at leaf node:
# minimu samples in aleaf node; affects generalization
# low value---small leaves may overfit,high value---smoother output
# example:min_samples_lead=1  memorize noise;min_samples_leaf=5
# prevent overfiiting
# tip=1-5% of dataset for classification tasks



# confusion matrix--->
# how much model confuse in which class
# true positive-->mean model ny prodiction ke wo tek hy 
# true negative-->model predict its not avaialble
# flase positive-->model ny wrong predict keya  mdoel bolta class hei or class nahi thi
# false negative--> model kehta moujooed nahi or class moujood thi

# GridSearchCV tumhare bataye hue hyperparameters ke saare combinations par model ko bar-bar check karke sabse 
# best accuracy wali setting automatic dhoond kar deta hai.


# coding--------------------->
# random forest tunning

import sklearn
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report



# laod dataset
data=load_breast_cancer()
x=data.data
y=data.target
# feature_names=data.feature_names

x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=42, stratify=y
)



# define parameter grid for tunning

param_grid={
    "n_estimators":[50,100,200],   # number of trees
    "max_depth":[None,5,10,20],     # tree depth
    "min_samples_split":[2,5,10],     #minimu sample to split
    "min_samples_leaf":[1,2,5]         #minimum sample at leaf

   
}



# grid search for best parameters

rf=RandomForestClassifier(random_state=42,n_jobs=-1)
grid=GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,                        #5-fold cross validation  4 pe train krega ek pe test pe krega
    scoring="accuracy",
    n_jobs=-1
)
grid.fit(x_train,y_train)


# best model evaluation and accuracy
best_model=grid.best_estimator_
y_pred=best_model.predict(x_test)
print("best parameter found")
for k,v in grid.best_params_.items():
    print(f"{k}:{v}")

print("test performance")
print(f"accuracy:{accuracy_score(y_test,y_pred):.4f}")

print(classification_report(y_test,y_pred))
