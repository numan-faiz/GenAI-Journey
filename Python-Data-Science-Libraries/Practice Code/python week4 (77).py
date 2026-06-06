# introduction to seaborn visualization library
# it is used for plots and graph its is advance version of matplotlib

# why seaborn
# cleaner visuals with minimal code
# build in theme and color palettes
# high level statistical plots
# idea For EDA in AI/ML pipelines


# key features
# high level plotting functtions
# automatic handling of pandas data frames
# built-in themes darkgrif,white grid,dark white ticks integrate with pandas,numpy and matplotlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(
    "healthcare_dataset.csv"
)
# print(df.info())

df=df.sample(500)
#axes-level example(scatterplot)
sns.scatterplot(
    data=df,
    x="Age",
    y="Room Number",
    hue="Blood Type"
)
plt.title("Age vs room number")
plt.show()


# figure-level example(relplot) used for alag alag column
sns.relplot(
    data=df,
    x="Age",
    y="Room Number",
    hue="Blood Type",
    col="Gender"
)
# now apply seaborn theme
sns.set_theme(style="whitegrid")
plt.show()


# recreating a matplotlib in seaborn
# matplotlib
plt.scatter(df["Age"],df["Room Number"])
plt.xlabel("Age")
plt.ylabel("Room Number")
plt.show()


# seabron
sns.scatterplot(
    data=df,
    x="Age",
    y="Room Number"
)
plt.show()
