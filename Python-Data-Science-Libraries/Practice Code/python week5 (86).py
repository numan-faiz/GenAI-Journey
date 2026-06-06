# train-test split data leakage prevention
# large data--->training
# small data--->testing
import pandas as pd
import numpy as np
df=pd.read_csv(
    "telecom_customer_churn_feature_engineering.csv"
)

print(len(df))
# we will split this into 960 training rows (80%)| 20% 240 testing rows
df_shuffled=df.sample(frac=1,random_state=42)

train_size=int(0.8*len(df_shuffled))
train_df=df_shuffled.iloc[:train_size]
test_df=df_shuffled.iloc[train_size:]

print(len(train_df),len(test_df))

# verify no overlap
set(train_df.index).intersection(set(test_df.index))


# leakage example--wrong practice
# wrong-scaling before split
income_mean=df["monthly_income"].mean()
income_std=df["monthly_income"].std()

df["income_scaled_wrong"]=(
    df["monthly_income"]-income_mean
)/income_std

print(df[["monthly_income","income_scaled_wrong"]].head())

 # correct approach
 # separate features and traget
x_train=train_df.drop("churn",axis=1)
y_train=train_df["churn"]
x_test=test_df.drop("churn",axis=1)
y_test=test_df["churn"]

print(x_train.shape,x_test.shape)

# target is safely isloated
# no leakage risk
