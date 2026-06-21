# decision trees-->implementation with sickit  learn
# decison tree sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


# 1-->Load dataset

data=load_iris()
x=data.data
y=data.target
feature_names=data.feature_names
class_names=data.target_names

# split into train and tests sets
x_train,x_test,y_train,y_test= train_test_split(
    x,y,test_size=0.3,random_state=42,stratify=y
)



# fit decision tree model
model=DecisionTreeClassifier(
    max_depth=3,
    criterion="entropy",
    random_state=42
)
model.fit(x_train,y_train)


# visulize the decision tree
plt.figure(figsize=(12,8))
plot_tree(
    model,
    feature_names=feature_names,
    class_names=class_names,
    filled=True,
    rounded=True
)
plt.title("Decision tree visulaization (Iris dataset)")
plt.tight_layout()
plt.show()


# evaluate model performance
y_pred=model.predict(x_test)

print("\n model performance")
print(f"accuracy:{accuracy_score(y_test,y_pred):.3f}\n")

print("confusion matrix")
print(confusion_matrix(y_test,y_pred))
print("\n classification report: ")

print(classification_report(y_test,y_pred,target_names=class_names))
