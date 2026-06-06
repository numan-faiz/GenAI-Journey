# customizing and exporting matplotlib visualization
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,50)
y=np.sin(x)
fig,ax=plt.subplots(figsize=(6,4))
ax.plot(x,y,label="sin(x)",color="b",linewidth=2)



# customize ticks and rotation

ax.set_xticks(range(0,11,2))
plt.xticks(rotation=30)


# legend placement
ax.legend(loc="upper right")


# label and title
ax.set_title("cutomize sine wave plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")


# save polished figure
plt.tight_layout()
plt.savefig("sine_plot.png",dpi=300,format="png")
plt.show()



import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)
fig,ax=plt.subplots()
ax.bar(
    df["category"].value_counts().index,
    df["category"].value_counts().values,
)
ax.set_xlabel("price shows")
ax.set_ylabel("price methods")
ax.tick_params(axis="x",rotation=45)
plt.show()

