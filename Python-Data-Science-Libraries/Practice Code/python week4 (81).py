# encoding categorical variable
# data science tools work only with numerical data so we convert text data into numerical form
# encoding is essential before training a model on a dataset
# catgeorical varaible such as gender,city country and payment type must be converte
# dencoding impacts model accuracy and interpretability
# machine learning models operaate only on a numerical data



# common methods of encoding
# one hot encoding--> it applied on unorder catgoeires we make  binary column for each category
# ordinal encoding-->its applied on order data
#   key consideration before encoding
# combine rare categories into "other"
# be aware of the curse of dimentionality in high cardinality feature
# always inspect the data after encoding using head(), or .info()


# sample data
import pandas as pd
df=pd.DataFrame({
    "city":["lahore","karachi","islamabad","lahore","karachi"],
    "segment":["A","B","A","C","B"],
    "sales":[200,240,180,300,220,]
})
print(df)

# one-hot encode
encoded=pd.get_dummies(df,columns=["city","segment"],drop_first=True)
print(encoded)



from sklearn.preprocessing import OrdinalEncoder
df2=pd.DataFrame({
    "size":["small","medium","large","medium","large"]
})
print(df2)

encoder1=OrdinalEncoder(categories=[["small","medium","large"]])
df2["Size_encoded"]=encoder1.fit_transform(df2[["size"]])
print(df2)