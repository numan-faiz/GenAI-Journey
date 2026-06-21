# k-NN--->impelemntaion with scikit learn
# steps for implementing k-nn

# load dataset--->split-->normalize-->train--->predict-->evaluate


# hyper parameter tunning-->
# select ptimal k using cross validation
# choose an appropirate distance merics (euclidean,manhatatan,minkowski)

# performance steps:
# normalize feature
# reduce dimensionality,
# feature selection
# k-NN--->impelemntaion with scikit learn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


data=load_digits()
x=data.data
y=data.target

# train_test_splittest
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42,stratify=y
)


# Feature scaling is important for distance-based mdoels

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)



print("trainning samples:",x_train.shape[0])
print("feature per sample",x_train.shape[1])


# train k-nn model

knn=KNeighborsClassifier(n_neighbors=5,metric="euclidean")
(knn.fit(x_train,y_train))


# make predictions
y_pred=knn.predict(x_test)



# evaluate performance

acc=accuracy_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)


print("k-NN accuracy :",round(acc,4))

print("confusion matrix: ",cm)


