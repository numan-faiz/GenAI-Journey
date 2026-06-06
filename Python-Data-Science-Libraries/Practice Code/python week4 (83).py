# feature transformation
# purpose of transformation
# reduce skewness
# handle outlier--->data righ or left skewed
# common tranformation
# # log transform
# 1. Log Transformation
# Ye sab se purana aur asaan tareeqa hai. Ye tab use hota hai jab aapka data Right Skewed ho
# (yani zyada tar values choti hon lekin kuch values bohat
# bari hon, jaise Salary ya Population).
# box-cox/yeo jhonson method
# Box-Cox Transformation
# Ye Log transform ka "Advanced Version" hai. Ye khud hi decide karta hai ke data par konsi power apply
# karni hai taake wo normal ho jaye.
# outlier handling method
# clipping,winsorization
# 1. Clipping (Standard Limits)
# Clipping mein hum khud se do values (Lower aur Upper) fix kar dete hain. Jo value boundary se bahar jati hai,
# use boundary wali value par set kar diya jata hai.
# Winsorization (Percentile Based)
# Winsorization bilkul clipping ki tarah hai, lekin isme limits hum khud se nahi dete balkay percentiles
# (percentage) par chortay hain.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv(
    "telecom_customer_churn_feature_engineering.csv"
)
print(df[["monthly_income","monthly_bill"]].describe())

# max>>mean
# strong skew present
# ideal candidates for transformation

# safe log transformation

import numpy as np
df["income_log"]=np.log1p(df["monthly_income"])
print(df[["monthly_income","income_log"]].head())

# before vs after
print(df[["monthly_income","income_log"]].describe())


# clipping
upper_limit=df["monthly_income"].quantile(0.99)
df["bill_clipped"]=df["monthly_income"].clip(upper=upper_limit)

result=df.loc[
    [df["monthly_bill"].idxmax(),
     df["monthly_bill"].sort_values().index[len(df)//2]],
     ["monthly_bill","bill_clipped"]

]
print(result)


# winsorization

from scipy.stats.mstats import winsorize
df["bill_winsor"]=winsorize(
    df["monthly_bill"],
    limits=[0.01,0.01]

)
# check effect on extreme value
result1=df.loc[
    [df["monthly_bill"].idxmin(),
    df["monthly_bill"].idxmax()],
    ["bill_winsor"]
]
import seaborn as sns
print(result1)
plt.figure(figsize=(10,4))
plt.subplot(1,2,2)
sns.histplot(df["bill_winsor"],kde=True,bins=30)
plt.title("monthly(winsorized)")

plt.tight_layout()
plt.show()