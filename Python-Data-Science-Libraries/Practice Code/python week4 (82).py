# feature scaling and normalization
# scaling ensures features are on similar range to improve distance-based model performance
# z-score standarization--->mean ko zero pe lany ke koshesh kerty hy
# min max scalling(normalization-->tamam value zero or 1 ke babarb kerty
# data leakge Risk
# aplying scaling on both tarining and test data together leads to data leakge,as test data information
# is used during training
# when and why to scale---->
# scale feature when using  distance-based models (KNN,SVM,PCA,clustering)
# avoid or handle careful;ly for tree-based models (decison tree ,random forest),as they are insentive to scale

import pandas as pd
import numpy as np
df=pd.read_csv(
    "telecom_customer_churn_feature_engineering.csv"
)
# print(df.info())

# inspect raw values focus---> income and bill value are an very diffrent scale
print(df[["monthly_income","monthly_bill"]].head())

# why scaling is required
print(df[["monthly_income","monthly_bill"]].describe())


# z-score scaling standarization(manual)
# clacualte mean and std
income_mean=df["monthly_income"].mean()
income_std=df["monthly_income"].std()
print("mean",income_mean)
print("std",income_std)

df["income_zscore"]=(df["monthly_income"]-income_mean)/income_std
print(df[["monthly_income","income_zscore"]].head())

# verify -score scaling
print(df["income_zscore"].mean(),df["income_zscore"].std())


# min-max scaling normal;ization
bill_min=df["monthly_bill"].min()
bill_max=df["monthly_bill"].max()

print("min",bill_min)
print("max",bill_max)

# apply min-max formula
df["bill_minmax"]=(df["monthly_bill"]-(bill_min)/bill_max-bill_min)
print(df[["monthly_bill","bill_minmax"]].head())

# verify min-max scaling
print(df["bill_minmax"].min(),df["bill_minmax"].max())

# show min,max and mid value together
result=df.loc[
    [df["monthly_bill"].idxmin(),
     df["monthly_bill"].idxmax(),
     df["monthly_bill"].sort_values().index[len(df)//2]],
     ["monthly_bill","bill_minmax"]

]
print(result)


# side by side comparison
print(df[["monthly_income","income_zscore","monthly_bill","bill_minmax"]].head())





# data_leakage-WRONG(scaling before split)
df_scaled_wrong=(df["monthly_income"]-df["monthly_income"].mean())/df["monthly_income"].std()
print(df_scaled_wrong.head())