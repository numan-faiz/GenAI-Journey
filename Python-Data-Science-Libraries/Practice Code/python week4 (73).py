# histogram and density plot
# histogram is one the most usefull concept in statistics in which we visualize frequency of data
# bins--->In a histogram, bins are the consecutive, non-overlapping intervals used
# to group a continuous range of data.
# density is used for normalize the data
import matplotlib.pyplot as plt
import numpy as np
group_A=np.random.normal(70,10,1000)
group_B=np.random.normal(80,12,1000)
plt.hist(group_A,bins=30,density=True,alpha=0.6,label="Group A")
plt.hist(group_B,bins=30,density=True,alpha=0.6,label="Group B")

plt.xlabel("score")
plt.ylabel("Density")
plt.title("distribution comparison")
plt.legend()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)
df=df.sample(n=1000)


# histogram revenue distribution
fig,ax=plt.subplots(figsize=(12,6))
ax.hist(df["price"],bins=30)
ax.set_title("revenue density distribution")
ax.set_ylabel("revenue")
ax.set_ylabel("density")
plt.show()


# density plot
fig,ax=plt.subplots(figsize=(12,6))
ax.hist(df["price"],bins=30,density=True,alpha=0.6)
ax.set_title("revenue density distribution")
ax.set_xlabel("revenue")
ax.set_ylabel("density")
plt.show()




# overlay two histogram(conparison)
# price vs category revenue
discounted_revenue=df["price"]*(1-df["review_count"])
fig,ax=plt.subplots(figsize=(10,4))
ax.hist(df["price"],bins=30,alpha=0.6,label=("original revenue"))
ax.hist(discounted_revenue,bins=30,alpha=0.6,label="discounted revenue")
ax.legend()
ax.set_title("comprison revenue")
plt.show()





