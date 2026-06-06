# outlier handling

# outlier are data points that significallly deviate from the normal data and lie at extreme value
# method of oulier-->
# clipping
# winsoriztion
# removal


import pandas as pd
import numpy as np
df=pd.DataFrame({

    # 5000 is outlier
    "sales":[100,200,150,300,5000,700,3000,1500,400,600]
})
print(df.describe())


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style(style="whitegrid")
plt.figure(figsize=(6,4))
sns.boxplot(y=df["sales"])
plt.title("box plot of sales (outlier visible)")
plt.show()


# cliping
from scipy.stats.mstats import winsorize

df['saled_clipped']=df['sales'].clip(upper=1000)
print(df)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
plt.figure(figsize=(6,4))
sns.boxplot(data=df["saled_clipped"])
plt.title("boxplot:original s clipped sales (upper=1000")
plt.show()



from scipy.stats.mstats import winsorize
df['sales_winsor']=winsorize(df['sales'],limits=[0,0.2])
print(df)

#removal outlier

df['sales_removed']=df['sales'].where(df['sales']<=1000,np.nan)
print(df)


import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
plt.figure(figsize=(8,5))
sns.boxplot(data=df[["sales","saled_clipped","sales_winsor","sales_removed"]])
plt.title("boxplot: original vs clipped vs winsorized sales vs sales removed")
plt.show()



import  pandas as pd
df= pd.DataFrame({
    "sales":[100,200,300,400,500,5000,100000]
})


# cliiping