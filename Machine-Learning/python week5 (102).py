# linear regression--implementation with scikit-learn


from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


X=np.array([[1],[3],[4],[5],[7]])
Y=np.array([3,5,7,9,11])


#   plot 1:scatter plot before regression-----
plt.figure(figsize=(6,4))
plt.scatter(X,Y,color='blue')
plt.title("scatter plot before linear regression")
plt.xlabel('X values')
plt.ylabel("Y-Values")

#plt.grid(True)
plt.show()




# now--->
model=LinearRegression()  #create a linear regression model instance
model.fit(X,Y)    # fit the model to the data
y_pred=model.predict(X)   # predict using the fitted model
print("predicted values: ",y_pred)


#------------plot2:scatter+best fit line

plt.figure(figsize=(6,4))
plt.scatter(X,Y,color='blue',label='original data')
plt.plot(X,y_pred,color='red',label="best fit line")
plt.title("scatter plot with regression best fit line")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
# plt.grid(True)
plt.show()


m=model.coef_
b=model.intercept_
print("slope of (m): ",m)
print("Y intercept (b): ",b)

