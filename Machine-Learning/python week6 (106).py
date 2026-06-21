# decision trees-tree depth and overfitting

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score



# create a toy dataset
x,y=make_moons(n_samples=500,noise=0.25,random_state=42)
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=42
)


# train test with diffrenet depth
depth=list(range(1,15))
train_acc=[]
test_cc=[]


for d in depth:
    model=DecisionTreeClassifier(
        max_depth=d,
        random_state=42
    )

    model.fit(x_train,y_train)


    train_pred=model.predict(x_train)
    test_pred=model.predict(x_test)


    train_acc.append(accuracy_score(y_train,train_pred))
    test_cc.append(accuracy_score(y_test,test_pred))
    print(test_cc)


# plot performance vs depth
plt.figure(figsize=(7,5))
plt.plot(depth,train_acc,label="training accuracy")
plt.plot(depth,test_cc,label="test acuuracy")
plt.xlabel("tree depth(max depth)")
plt.ylabel("accuracy")
plt.title("decision tree depth vs overfitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




# print key observation

best_depth=depth[np.argmax(test_cc)]
print(f"best depth based on test accuracy: {best_depth}")