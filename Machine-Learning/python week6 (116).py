# SVM---Margin Maximization Concept

# margin--->distance from hyperplane to nearest data point

# demonstration of SVM margin ,support vectors, and optimal hyperplane

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC



# generate a simple data set
x,y=datasets.make_blobs(
    n_samples=100,
    random_state=42,
    centers=2,
    cluster_std=1.1
)


svm=SVC(kernel="linear",C=10)  # large c approximates hard margin SVM
svm.fit(x,y)


# extract parameter of the hyperplane:w^T x+b=0
w=svm.coef_[0]
b=svm.intercept_[0]


# function to compute decision boundary
def decision_line(x):
    return-(w[0]*x+b)/w[1]



# create x-axis value

x_vals=np.linspace(x[:,0].min(),x[:,0].max(),100)
print(x_vals)


# compute margin lines
margin=1/np.linalg.norm(w)

# np.linalg.norm(w) ka matlab hai vector w ki length (magnitude) nikalna.


# lines parrallel to the decison boundary at distance =margin
y_vals=decision_line(x_vals)
y_margin_pos=y_vals+margin
y_margin_neg=y_vals-margin




# visualization
plt.figure(figsize=(6,5))

# plot data points
plt.scatter(x[:,0],x[:,1],c=y,cmap="bwr",edgecolors="k")



# plot optimal hyperplane
plt.plot(x_vals,y_vals,"k--",label="optimal hyperplane")



# plot margins
plt.plot(x_vals,y_margin_pos,"k:",label="margin boundary")
plt.plot(x_vals,y_margin_neg,"k:")



# highlight support vectors
plt.scatter(
    svm.support_vectors_[:,0],
    svm.support_vectors_[:,1],
    s=120,
    facecolors="none",
    edgecolors="black",
    linewidths=1.5,
    label="support vectors"

)

plt.title("SVM, maximum margin classifier")
plt.legend()
plt.show()