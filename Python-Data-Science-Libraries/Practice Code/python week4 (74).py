# creating subplots and layouts
# plots ke ander subplots
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)
fig,axs=plt.subplots(2,2,figsize=(8,6))


#line plot
axs[0,0].plot(x,y,color="b")
axs[0,0].set_title("line plot")


axs[0,1].scatter(x,y,color="r")
axs[0,1].set_title("scatter plot")
# histogram
axs[1,0].hist(np.random.randn(200),bins=20,color="g")
axs[1,0].set_title("histogram")

# bar chart
categories=["A","B","C"]
values=[5,3,7]
axs[1,1].bar(categories,values,color="m")
axs[1,1].set_title("bar chart")

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(
    "IPL.csv",
    parse_dates=["date"]
)
# print(df.info())


# bsic subplots grid(2 by 2 example)
fig, axes=plt.subplots(2,2,figsize=(8,6))
axes[0,0]
axes[1,1]

# hands_on dashboard example
fig,axes=plt.subplots(2,2,figsize=(12,8))

# first innings score  distribution
axes[0,0].hist(df["first_ings_score"],bins=20,color="g")
axes[0,0].set_title("first_ings_score distribution")

# monthly price trend
monthly=(
    df.set_index("date")["first_ings_score"]
    .resample("ME").sum()
)
axes[0,1].plot(monthly.index,monthly.values,color="r")
axes[0,1].set_title("monthly score show")


#margin shows
axes[1,0].hist(df["margin"],bins=10,color="m")
axes[1,0].set_title("margin shows distributuion")


# highscore ratinng
axes[1,1].hist(df["highscore"],bins=10,color="y")
axes[1,1].set_title("highscore rating")


# shared axes(sharex,sharey)
fig,axes=plt.subplots(1,2,sharey=True)
fig,axes=plt.subplots(1,2,sharey=False)

# layout management
plt.tight_layout()
plt.show()