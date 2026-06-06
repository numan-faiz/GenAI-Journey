# categorical data visulaization with seaborn
# families of categorical grapgh--->
# aggregate(central tendency grapghs)-->
# bar plot,count plot available in aggregate
# distribution plot
# box plot,violin plot,swarm plot,strip plot


# 1. Aggregate Plots (Central Tendency)
# Ye graphs data ko summarize karke unka "average" ya "total" dikhate hain.
#
# Bar Plot (sns.barplot): Har category ka mean (average) dikhata hai aur sath mein error bar se variation bhi
# show karta hai.
#
# Count Plot (sns.countplot): Ye sirf counting karta hai—matlab har category ki frequency (kitni baar wo
# cheez aayi hai) dikhata hai.
#
# 2. Distribution Plots
# Ye graphs dikhate hain ki data ki values kaise spread (phaili) hui hain.
#
# Box Plot (sns.boxplot): Data ko quartiles mein divide karta hai; ye "outliers" (ajeeb values)
# aur median dekhne ke liye best hai.
#
# Violin Plot (sns.violinplot): Box plot aur density plot ka combo hai; ye data ka hump/shape
# dikhata hai ki zyada values kahan jama hain.
#
# Strip Plot (sns.stripplot): Har data point ko ek single dot ki tarah dikhata hai (chote datasets ke liye
# accha hai).
#
# Swarm Plot (sns.swarmplot): Strip plot jaisa hi hai, lekin dots ek dusre ke upar overlap nahi hote,
# balki side-by-side adjust ho jate hain (behtar visibility).


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(
    "healthcare_dataset.csv"
)
df=df.sample(500)
# barplot vs countplot
# countplot
sns.countplot(
    data=df,
    x="Blood Type",

)
plt.title("count plot of Blood Type")
plt.show()


# barplot
sns.barplot(
    data=df,
    x="Blood Type",
    y="Hospital",

)
plt.xticks(rotation=30)
plt.title("bar plot for hospital and blood group")
plt.show()


# boxplot
sns.boxplot(
    data=df,
    x="Blood Type",
    y="Hospital"
)
plt.xticks(rotation=30)
plt.title("box plot for blood group and haspatal")
plt.show()

# violin plot

sns.violinplot(
    data=df,
    x="Blood Type",
    y="Hospital"

)
plt.xticks(rotation=30)
plt.title("violin plot")
plt.show()



# swarm/strip plot
sns.stripplot(
    data=df,
    x="Blood Type",
    y="Hospital",
    jitter=True
)
plt.xticks(rotation=30)
plt.title("strip plot hy ")
plt.show()

# side by side comparison of box and strip
sns.boxplot(
    data=df,
    x="Blood Type",
    y="Hospital"
)
sns.stripplot(
    data=df,
    x="Blood Type",
    y="Hospital",
    color="black",
    alpha=0.4

)
plt.xticks(rotation=30)
plt.show()