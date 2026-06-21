# Naive--Bayes--Feature independence assumption

# understanding the assumptions:
# naive bayes assumes each future contributes independently to the classification
#  example: in spam detetion "win", and "prize" are treated as unrealted words



# how to show it in ML coding lets go
# simplifies probablity computation:
# ignores possible relationships between features

# demosntation of naive bayes and the feature independence assumption
import numpy as np 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


# load dataset
data=load_breast_cancer()
x,y=data.data,data.target
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42,stratify=y
)

print("number of features:",x_train.shape[1])


# train naive basie classifier
nb=GaussianNB()
nb.fit(x_train,y_train)



# evaluate performance
y_pred=nb.predict(x_test)
acc=accuracy_score(y_test,y_pred)

print(f"naive bayes accuracy:,{acc:.4f}")


# show learned probablities ( for intution)


print("class prior probablities p(y)")
print(nb.class_prior_)


print("feature means per class (sample of first 5 features):")
print(nb.theta_[:,:5])
print("feature variance per class (sample of first 5 features):")
print(nb.var_[:,:5])




# =====================================================================
# KNN/Naive Bayes Applied Trick: Rules of X and Y
# =====================================================================

# 1. Training Step:
#    model.fit(x_train, y_train)  -> (Train Questions, Train Answers)

# 2. Prediction Step:
#    y_pred = model.predict(x_test) -> (Test Questions ONLY)

# 3. Accuracy Step:
#    accuracy_score(y_test, y_pred) -> (True Answers, Computer's Answers)

# ---------------------------------------------------------------------
# Naive Bayes Brain Parameters:
# ---------------------------------------------------------------------
# nb.class_prior_ -> Baseline probability of each class P(y)
# nb.theta_       -> Mean (Average) of each feature for each class
# nb.var_         -> Variance (Spread) of each feature for each class
# :.4f            -> Format code to display only 4 digits after dot (.)