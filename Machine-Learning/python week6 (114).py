# random forest---implementation with scikit learn


# steps for impelemnting random forest
# load data-->train
# model-->tune
# parameters-->evalaute
# performance--->interpret results


# key takeaways


# start with defualt parametrs
# tune based on oob error or cross validation
# check accuracy and confusion matrix
# use feature importance


# precision---->out of all predicted positives,how many are actually correct
# precision=tp/tp+(fp)

# example-->blocking real user

# recall--->
# out of all actual positives,how many are correctly detected
# recall=tp/tp+fn
# example-->disease detection
# F1-score---> harmoic mean of precison and recall
# represents the balance between precison and recall
# f1=2*precison+recall?precison*recall
# best suited for imbalanced datasets


# support:
# number of actuall samples per class
# helps in understanding data distribution


# random forest---implementation with scikit learn
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

data=load_iris()
x=data.data
y=data.target
feature_names=data.feature_names
class_names=data.target_names

x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42,stratify=y
)

print("taiining samples:",x_train.shape[0])
print("test samples:",x_test.shape[0])


# fit baseline random forest
rf=RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42
)
rf.fit(x_train,y_train)



# evaulate performance
y_pred=rf.predict(x_test)
acc=accuracy_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)

print("random forest accuracy:", round(acc,4))
print("confusuion matrix: ",cm)



# simple parameter tunning (n_estimators)
best_acc=0
best_n=None

for n in [20,50,100,200]:
    model=RandomForestClassifier(
        n_estimators=n,
        random_state=42
    )
    model.fit(x_train,y_train)
    pred=model.predict(x_test)
    acc_n=accuracy_score(y_test,pred)

    print(f"n_estimator={n}:accuracy={acc_n:.4f}")

    if acc_n>best_acc:
        best_acc=acc_n
        best_n=n


print(f"best n_estimator selected:",best_n)





# feature importance
importances=rf.feature_importances_
idx=np.argsort(importances)

plt.figure(figsize=(6,4))
plt.barh(feature_names,importances)
plt.title("feature importance  (iris+random forest)")
plt.tight_layout()
plt.show()