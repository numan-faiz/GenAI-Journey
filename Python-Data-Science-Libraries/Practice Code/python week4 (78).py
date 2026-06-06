# distribution plot-histplot and KDEPlot
# histogram plot make histogram of data with multiple stack and layerd group
# while sns.kdeplot make a kernel density etimate
# sns.ecdfplot-->empricial cmulative disttribution function-->add up distribution


# istplot: Sirf bheed dikhata hai "bars" mein.
#
# KDE Plot: Bheed ko ek "lehair" (wave) ki tarah dikhata hai.
#
# ECDF Plot: Ye dikhata hai ki data "jama" (accumulate) kaise ho raha hai 0 se 100% tak.
H

# common argument
# multiple--> 'layer','stack','dodge'
# stat-->count,density probabiltiy ideal for understanding datashape spread and skewness
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(
    "healthcare_dataset.csv"
)

# histplot
# scenarion age distribution
sns.histplot(
    data=df,
    x="Age",
    bins=30
)
plt.title("Age distribution")
plt.show()

# comparing distribution

# make two histogram in one grapgh
sns.histplot(
    data=df,
    x="Age",
    hue="Gender",
    multiple="stack",
    bins=30
)
plt.title("distribbution analysis")
plt.show()



# kernal distribution to smooth grapgh
sns.kdeplot(
    data=df,
    x="Age",
    hue="Gender",
    fill=True
)
plt.title("kernal distribution")
plt.show()

# ECDF--Shows comulative prportion  we add distribution over a period of time
sns.ecdfplot(
    data=df,
    x="Age",
    hue="Gender"
)
plt.title("ECDF graph")
plt.show()