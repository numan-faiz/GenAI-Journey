# SVM-->support vector machine
# SVM ka asal kaam data points ke darmayan ek aisi sabse best boundary (deewar) khari karna hai jo dono 
# classes ko aik doosre se  zyada se zyada door alag kar sake."

# support vector machines (SVMs) are supervised learning alogoritham used for classification and sometimes regression
# SVM finds the optiomal plane hyperplane (deewaar line,point,suurface) that separatesclasses by maximizing the margin
# bteween them


# support vector machine are the data points closest to the hyperplane; they define its position and influence
#  classification
# SVM works well in high-dimentional spaces and with non-linearly separable data using kernels


# hyperplane ka mtlb deewar data agar one dimentionn hu ty hyper plane ek point hga or 2D hu tu hyper
#  plane ek line hga agar 3d hu tu hyperplane ek surface hga ju data ya 2 points   ko alag krega 

# MArgin
# distnace between the hyerplane and the nearest data points of any class
# SVM maximize this margin to improve genralization on unseen data

# large margin--->lower generalization error;samll margin-->sensitivity to noise/outliers
# SVM vectors lie  on the margin and are crtical for defining it


# Suppoer vector machine-->
# only suppoert vectors matter,rremoving other point does not affect the hyperplane
# SVM optimization focuses soley on thes critical points


# mathematical equation of SVM:-->
# hyperplane equation=w.x+b=0
# x is a feature vectore,w is the weight vector b is bias



# optimization problem:
# goal:to  maximize the margin between classes the svm minimize the objective function

# 1/2 ||w||*2


# constraint:the solution must satisfy  yi(wtxi+b)>=1, ensuring all points are correctly classified



# support vectors-->:only points lying exactly on the margin yi(wtxi+b)=1 are the suport vectors

# influence:these few support vectors determine the final w and b;non support vectors do not affect the result


# summary of margin maximization:
# the margin is the distance from the hyperplane to the rest nearest data points
# the goal is to select the hyperplane that maximize this margin for better generalization
# the support vectors are the critical,nearest points that define the final hyperplane
# optimization acheives this by minimizing subject to the classification constraint


