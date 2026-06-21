# Naive bayes---implementaion with sciket learn

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report



# laod dataset
# brest ancer dataset is a real word medical dataset
data=load_breast_cancer()
# features and target
x=data.data
y=data.target

# convert to Dataframe for better understanding
df=pd.DataFrame(x,columns=data.feature_names)

df['target']=y

print(df.shape)
print(df.head())



# dataset infromation
print("target classes")
print(data.target_names)
print("class distribution")
print(df['target'].value_counts())


# Naive bayes
# 4.split dataset into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42,stratify=y
)

print("trainning samples:",x_train.shape[0])
print("testing samples:",x_test.shape[0])


# create and train naive bayes mdoel
nb_model=GaussianNB()
nb_model.fit(x_train,y_train)
print("naive bayes model trainnind completed")


# make predictions
y_pred=nb_model.predict(x_test)
print("first 10 predictions")
# print(y_pred[:10])
# 
# Model evaluation
# Accuracy
accuracy=accuracy_score(y_test,y_pred)
print("model accuracy:",round(accuracy*100,2),"%")


cm=confusion_matrix(y_test,y_pred)


print("confusion matrix",cm)


# detli classifiaction matrics
print("classification report:")
print(classification_report(y_test,y_pred))



# interpretaion of confusion matrix
print("interpretaion of confusion matrix")

print("true negative:",cm[0][0])
print("true positive:",cm[0][0])
print("true positive:",cm[0][0])
print("false negative:",cm[1][1])


# 9.predict on new sample
sample=x_test[0].reshape(1,-1)
prediction=nb_model.predict(sample)


print("predictions for a new sample")