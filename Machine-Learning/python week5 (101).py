# linear regression-python implementation from scratch

# workflow for python implementation
# 1.load data
# 2.define hypothesis (y=mx+b)
# 3.define cost function
# 4.apply gradient descent

# derivtive(gradient):
# derivative for slope:

        #  n
# Dm= -²⁄ₙ ∑  xᵢ · (yᵢ - ŷᵢ) 
        # i=0



# derivative for intercept:
        #  n
# Dm= -²⁄ₙ ∑  (yᵢ - ŷᵢ) 
        # i=0




 # coding start from here

import numpy as np
learning_rate=0.01   #step size

epochs=5 # number of iterations

X=np.array([1,2,3,4,5])  #input data
Y=np.array([3,4,2,5,6])    #target data

m,b=0.0,0.0 #initial parameters
n=len(X) # number of  data points



for i in range (epochs):
    y_pred=m*X+b
    cost=((y_pred-Y)**2).mean()
    darivate_m=-2/n*sum(X*(Y-y_pred)) # derivativ with respect to M
    darivate_b=-2/n*sum(Y-y_pred)   # derivative wrt b
    m-=learning_rate*darivate_m
    b-=learning_rate*darivate_b

    print(f"epoch {i+1}/{epochs},Cost:{cost},m:{m},b: {b}")




