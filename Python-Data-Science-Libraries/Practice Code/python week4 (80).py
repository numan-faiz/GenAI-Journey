# Headtp and corelation visulaization
# heatmap is to help the correlation od fata to display
# 1. Correlation (df.corr())
# One-liner: Ye ek mathematical matrix hai jo batati hai ki jab ek value badhti hai, toh dusri par
# kya asar padta hai.
#
# Iska score -1 se +1 ke beech hota hai.
#
# +1: Perfect rishta (Ek bada toh dusra bhi bada).
#
# 0: Koi rishta nahi.
#
# -1: Ulta rishta (Ek bada toh dusra kam hua).
#
# 2. Heatmap (sns.heatmap)
# One-liner: Ye correlation matrix ko rangon (colors) mein convert kar deta hai taaki humein aankhon se
# turant samajh
# aa jaye ki kahan "garmi" (high correlation) hai.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(
    "healthcare_dataset.csv"
)

numeric_df=df[[
    "Age","Billing Amount","Room Number"
]]
corr_matrix=numeric_df.corr()
print(corr_matrix)

# heatmap--basic visualization
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)
plt.title("correlation heatmap (health data)")
plt.show()



# masking uppar traingle
import numpy as np
mask=np.triu(np.ones_like(corr_matrix,dtype=bool))

sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    cmap=("coolwarm")
)
plt.title("correlation heatmap (Masked)")
plt.show()