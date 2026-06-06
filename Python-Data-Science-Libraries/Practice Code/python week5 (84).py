# Creating new features from existing data
# how to add some extra features in our data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv(
    "telecom_customer_churn_feature_engineering.csv"
)
df["signup_date"]=pd.to_datetime(df["signup_date"])
df["signup_year"]=df["signup_date"].dt.year
df["signup_month"]=df["signup_date"].dt.month
df["signup_day"]=df["signup_date"].dt.dayofweek

print(df[["signup_date","signup_year","signup_month","signup_day"]].head())

# ratio feature creation
df["bill_to_income_ratio"]=(
    df["monthly_bill"]/df["monthly_income"]
)
print(df[["monthly_bill","monthly_income","bill_to_income_ratio"]].head())


# interaction feature
df["support_bill_interaction"]=(
    df["support_tickets"]*df["monthly_bill"]
)
print(df[["support_tickets","monthly_bill","support_bill_interaction"]].head())


# text lentgh feature for feedback length
df["feedback_length"]=df["customer_feedback"].str.len()
print(df[["customer_feedback","feedback_length"]].head())

# keyword flag feature
df["complain_flag"]=df["customer_feedback"].str.contains(
    "slow|poor|expensive|unreliable|drops",
    case=False
).astype(int)

print(df[["customer_feedback","complain_flag"]].head())