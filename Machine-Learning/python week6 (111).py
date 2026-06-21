# random forest-- how it works part 2

# building multiple tree on  diffrenet subsets
# each tree is trained on a different bootstrapped dataset with random feature selection
# example:features[income,age,credit score,debt]
# tree1 use[income,age]
# tree2 uses[credit score,debt]
# diversity in both data and feature ensure robustness ensemble
# random feature selection reduces bias from individual features


# Aggregating prediction classification-->
# final output is based on majority voting 
# aggregation reduces errors from individual

# aggregating predictions regressions
# example:-->house prices
# [300k,310k,290k,305k,295k]-->prediction-300k

# Advantages of random forest aggregation-->
# aggregation reduces variance and improve accuracy
# robust noise data and outliers
# efficienly handle high dimentiinal datasets(mean more more feature in dataset is high dimentional)
# feature importace ranking and 00b valiadtaion enhance interpretability and performance
#  key takeways(faiday):
# many uncorrelated tree are trained on bootstrapped samples
# provide low variance ,high accuracy and robust prediction




# towrads coding-->

# random forest
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# load dataset
data=load_breast_cancer()
x=data.data
y=data.target
feature_names=data.feature_names

x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=42,stratify=y
)

rf=RandomForestClassifier(
    n_estimators=50,   # number of tree in the forest
    max_depth=None,     # allow full tree
    bootstrap=True,      #samopling with replacement(bootstrapping)
    criterion='entropy',
    random_state=42,
    n_jobs=-1
)
rf.fit(x_train,y_train)




# make predictions majority
y_pred=rf.predict(x_test)
print(y_pred)


# evaluate performance
print("random forest performance")
print(f"Accuracy:{accuracy_score(y_test,y_pred):.3f}\n")

print("confusion matrix")
print(confusion_matrix(y_test,y_pred))
print("classification report")
print(classification_report(y_test,y_pred))




# show how trees contribute(model insight)

print("feature importance (average accross all tree) ")
for name,imp in sorted(zip(feature_names,rf.feature_importances_),
                      key=lambda x:x[1],reverse=True)[:5]:
    print(f"{name}:{imp:.4f}")


    