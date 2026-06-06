#  Mini Project - Loan Risk Analysis & Feature Engineering

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('loan_data.csv')
print(df.info())


df['income']=df['income'].fillna(df['income'].median())
print(df.info())


# visualizing correlation
plt.figure(figsize=(8,4))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm", fmt=".2f")
plt.title("visualizing correlation")
plt.show()

plt.figure(figsize=(8,4))
sns.boxenplot(x=df['loan_amount'])
plt.title("check outlier in laon amount")

qu_limit=df['loan_amount'].quantile(0.90)
ql_limit=df['loan_amount'].quantile(0.5)
df["clean-loan_amount"]=df['loan_amount'].clip(upper=qu_limit,lower=ql_limit)


plt.figure(figsize=(8,4))
sns.boxenplot(x=df['clean-loan_amount'])
plt.title("identify outlier in laon amount")
plt.show()

# feature engineering
df["dti_ratio"]=df['clean-loan_amount']/df['income']
bins=[300,580,670,740,850]
labels=['high','low','moderate','good']

df['risk_category']=pd.cut(df['credit_score'],bins=bins,labels=labels)
print(df[['income','dti_ratio','risk_category']].head())



# now findigs summary
summary=df.groupby('risk_category',observed=False)['default'].mean()*100
print(f"defualt percentage by risk category:\n{summary}")