# SVM---The Kernel Trick Explained


# introduction to kernels:
# issue:datasets that are not linearly separable cannot be classified directly by a linear SVM

# solution:
# the kernel trick maps the original feature to a higher dimentional space


# mechanism:in this new space,the data becomes linearly separable by a hyper plane

# efficiency:
# A kernel function k(xi,xj)  computes the inner product efficeintly avoiding explicit,complex coordinate
#  transformation


## Common Kernel Functions (SVM ke Kernels)

### 1. Linear Kernel

# * **Formula:** $K(x_i, x_j) = x_i^T x_j$
# * **Asan Matlab:** Yeh tab use hota hai jab data ke beech me bilkul seedhi boundary line khainchni ho aur
# data aasan ho.

### 2. Polynomial Kernel

# * **Formula:** $K(x_i, x_j) = (x_i^T x_j + c)^d$
# * **Asan Matlab:** Yeh data ko higher dimensions me le ja kar **curved (tedhi-medhi/gool)** boundaries 
# banata hai taake complex data divide ho sake.


### 3. RBF / Gaussian Kernel

# * **Formula:** $K(x_i, x_j) = \exp(-\gamma \|x_i - x_j\|^2)$
# * **Asan Matlab:** Yeh dunya ka sabse mashhoor aur **default kernel** hai, jo boht zyaada complex
#  aur ghul-milay hue (non-linear) data ko behtareen tareeqe se alag karta hai.

### 4. Kernel Choice

# * **Asan Matlab:** Sahi kernel select karna boht zaroori hai, kyunki isi par depend karta hai ke aapka SVM 
# mushkil aur complex data ko kitni safai se divide karega.




# coding:
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



# create non linear separable data
x,y=make_circles(n_samples=200,random_state=42,factor=0.3,noise=0.05)

plt.figure(figsize=(5,4))
plt.scatter(x[:,0],x[:,1],c=y,cmap="bwr",edgecolors="k")
plt.title("original data (not linearly separable)")
plt.show()


# train SVM with the diffrenet kernals
kernels={
    "linear":SVC(kernel="linear"),
    "polynomial":SVC(kernel="poly",degree=3),
    "RBF":SVC(kernel="rbf",gamma=1.5)
}

for name,model in kernels.items():
    model.fit(x,y)
    y_pred=model.predict(x)
    acc=accuracy_score(y,y_pred)
    print(f"{name} kernal accuracy:{acc:.3f}")




    # visualize decison boundary for RBF kernel

rbf_model=kernels["RBF"]

# create a grid of points
xx,yy=np.meshgrid(
    np.linspace(x[:,0].min()-0.2,x[:,0].max()+0.2,200),
    np.linspace(x[:,1].min()-0.2,x[:,1].max()+0.2,200),
)


grid=np.c_[xx.ravel(),yy.ravel()]
z=rbf_model.predict(grid).reshape(xx.shape)



plt.figure(figsize=(5,4))
plt.contourf(xx,yy,z,alpha=0.3)
plt.scatter(x[:,0],x[:,1],c=y,cmap="bwr",edgecolors="k")

plt.scatter(
    rbf_model.support_vectors_[:,0],
    rbf_model.support_vectors_[:,1],
    s=80,facecolor="none",edgecolors="black"
)

plt.title("RBF Kernel:Nonlinear decison boundary")
plt.show()

