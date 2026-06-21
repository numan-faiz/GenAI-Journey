# SVM--implementaion with scikit learn


# using diffrenet kernels:
# linear
# polynomial
# RBF
# hyperparameter tunning

# steps to run svm-->load dataset->split-fit svm-predict-evaluate
# importance choices in SVM:
# sacle feature befor applying svm
# kernel choice,hyperparameter tunning,evaluation
# used gridsearccv for automated hyperparameter tunning


# SVM--implementaion with scikit learn
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix




# ----------------------loda dataset----
data=load_breast_cancer()
x=data.data
y=data.target
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42,stratify=y
)


print("training samples :", x_train.shape[0])
print("test samples: ",x_test.shape[0])




# 2#    train svmwith different kernels
models={
    "Linear":SVC(kernel="linear",C=1.0),
    "RBF":SVC(kernel="rbf",C=1.0,gamma=0.01),
    "poly":SVC(kernel="rbf",C=1.0,degree=3)
}

result={}

for name,model in models.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)

    acc=accuracy_score(y_test,y_pred)
    cm=confusion_matrix(y_test,y_pred)
    result[name]=(acc,cm)


# print evaluation results

for name,(acc,cm) in result.items():
    print(f"===={name} kernel====")
    print(f"accuracy: {acc:.4f}")
    print("confusion matrix: ")
print(cm)



