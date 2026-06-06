# outlier detection using statistical rule
# outlier are data points that full outside the normal range,representing extreme value that can distort
# the mean and median of the dataset
# it disturb mean and median annd median mode so we remove its when we identify outlier
# methods:
# IQR method--->by quantile
# z-score method
# domain-driven thresholds

# now how we do in pythod method
import pandas as pd
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)
print(df.info())

Q1=df["review_score"].quantile(0.25)
Q3=df["review_score"].quantile(0.75)
IQR=Q3-Q1
print(Q1,Q3,IQR)
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

# . Outliers Ko Identify Karna
outlier_iqr=df[(df["review_score"]< lower_bound) | (df["review_score"]> upper_bound)]

# for verifrication
print(outlier_iqr.shape)

print(outlier_iqr[["review_score","price"]].head())

# if we have outlier then we do this Outliers Ko Remove Karna
df = df[(df["review_score"] >= lower_bound) & (df["review_score"] <= upper_bound)]
print(df.shape)


# another method
# z-score method
from scipy.stats import zscore
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)
df["review_score_Z"]=zscore(df["review_score"])
outlier_z=df[df["review_score_Z"].abs()>3]
print(outlier_z.shape)

df=df[df["review_score_Z"].abs()>=3]
print(df.shape)

