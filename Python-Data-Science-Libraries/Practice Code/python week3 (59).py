# handling missing data
import pandas as pd
import numpy as np
df=pd.read_csv(
    "IPL.csv",
    parse_dates=["date"],
    dtype={
    "venue":"category",
    "margin":"category"
    }

)
print(df.info())


# for detecting missing value
print(df.isna().sum())

# fill missing value in columns or rows to be like
# mean is too sensitive
df['first_ings_score']=df['first_ings_score'].fillna(df['first_ings_score'].median())

print(df.info)

# fill missing value with mean of non numeric column first convert it into numeric
# df['margin']=pd.to_numeric(df['margin'])
# df['margin']=df['margin'].fillna(df['margin'].median()[0])
# print(df.info())


# fill missing value with median
# df['venue']=df['venue'].fillna(df['venue'].median())
# print(df.info)

# fill categorical value with mode
# df['category']=df['category'].fillna(df['category'].mode()[0])
# print(df.info())

# u also drop the null value
# df.dropna(subset='toss_decision',inplace=True)
# print(df.info())
print(df.isna().sum())
