# Descriptive Stats & Data Distributions
# to verify our dataset is fine
# some functions
# df.describe()
# df['col'].value_counts() use for count column value
# df.quantile(q)--->qunatile divde our dataset in equal portion
# skewness operator is used  for that data is on right or left side skewed tu nahi hy
# kurtosis--->we do kurtosis analysis also

import pandas as pd
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)
print(df.shape)
print(df.describe())


# for specific column
print(df[["price","review_score"]].describe())
# quantiles
print(df["price"].quantile([0.25,0.5,0.75]))

# identify skewness
print(df["price"].mean(),df["review_score"].median())


# positive value-->right skew
print(df["price"].skew())

# catgeory level descriptive statistics

# do diffrenet product categories behave diffrently
print(df.groupby("review_score")["price"].describe())

# find highest category
print(df.groupby("review_score")["price"].mean())


# using IQR to undertsand spread of data
Q1=df["review_score"].quantile(0.25)
Q3=df["review_score"].quantile(0.75)
IQR=Q1-Q3
print(Q1,Q3,IQR)

# for verfication to print true false
print(Q3>Q1) and (IQR>0)
