# line and scatter plots basics
# line grapaph-->make a line grapgh use less amount of plots

# line grapgh is use for linear trend and linear relation
# scatter grapgh-->use for more amount of plots
# scatter plot is used for relation between two complex variable


# line graph
import matplotlib.pyplot as plt
# sample data
days=[1,2,3,4,5,6,7]
sales=[4500,678,98723,954754,9383,95485,3644745]

plt.plot(days,sales,
         marker='o',
         linewidth=2,
         alpha=0.8,
         label="Daily sales"
         )

plt.title("sales trend over a weak")
plt.xlabel("day")
plt.ylabel("sales")
plt.legend()
plt.show()


# scatter grapgh
import matplotlib.pyplot as plt
# sample data
temprature=[20,25,30,35,40,45,45]
ice_cream_sales=[100,200,300,400,500,600,700]
plt.scatter(temprature,ice_cream_sales,
            alpha=0.7,
            marker='x',
            label="Sales Vs Temp"
            )

plt.title("Relationship between Temprature and Ice_cream")
plt.xlabel("Temprature")
plt.ylabel("Ice Cream Sales")
plt.legend()
plt.show()



# now for dataset make a grapgh

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(
    "IPL.csv",
    parse_dates=["date"]
 )
# print(df)
df=df.sample(n=70)


# line plot for monthly second_ings_score
monthly_second_ings_score=(
    df
    .set_index("date")["second_ings_score"]
    .resample("ME")
    .sum()
)
fig,ax=plt.subplots(figsize=(12,6))
ax.plot(monthly_second_ings_score.index,monthly_second_ings_score.values,linewidth=2,alpha=0.6)
ax.set_title("Monthly  second innings  score")
ax.set_xlabel("date")
ax.set_ylabel("second innings score")
plt.show()



# now scatter plot
fig, ax=plt.subplots(figsize=(12,6))
ax.scatter(df["date"],df["second_ings_score"],alpha=0.5)
ax.set_title("monthly iniings score")
ax.set_xlabel("Dates")
ax.set_ylabel("Score")
plt.show()

