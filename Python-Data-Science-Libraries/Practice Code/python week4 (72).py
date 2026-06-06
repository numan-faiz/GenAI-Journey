# Bar charts in matplotlib,grouped and stacked
# bar charts show data in the form of bars
# bar need is occur only when we grouping the data
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)

# now simple bar chart ---of price and category by both_revenue named
both_revenue=df.groupby("category")["price"].sum()
fig,ax=plt.subplots(figsize=(8,6))
ax.bar(both_revenue.index,both_revenue.values)

ax.set_title("total revenue by both_revenue")
ax.set_xlabel("category")
ax.set_ylabel("revenue")
plt.show()


# grouped bar chart--- revenue by category and sales_month_10 or region
grouped=df.groupby(["category","sales_month_10"])["price"].sum().unstack()
grouped.plot(kind="bar",figsize=(12,6))
plt.title("revenue by category and sales_month_10")
plt.ylabel("revenue")
plt.show()



# bar plot for stack ek ke uper dsri bar din 3esri
# stacked bar chart
grouped.plot(kind="bar",stacked=True,figsize=(12,6))
plt.title("stacked revenue by category and sales")
plt.ylabel("Revenue")
plt.show()