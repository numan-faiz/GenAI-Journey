# error bars and confidence intervals in plots
# we show the spread od error and confidence
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(
    "IPL.csv",
    parse_dates=["date"]
)

# error bars - mean revenue by highscore
stats=df.groupby("highscore")["first_ings_score"].agg(["mean","std"])
fig,ax=plt.subplots()
ax.bar(
    stats.index,
    stats["mean"],
    yerr=stats["std"],
    capsize=5
)

ax.set_title("average score revnue by highscore")
ax.set_ylabel("highscore")
plt.show()



df=df.head(n=60)
# confidance band--montly score trend with change
monthly=(
    df.set_index("date")["highscore"]
    .resample("ME")
    .agg(["mean","std"])
)

fig,ax=plt.subplots(figsize=(10,6))
ax.plot(monthly.index,monthly["mean"],label="mean highscore")

ax.fill_between(
    monthly.index,
    monthly["mean"]-monthly["std"],
    monthly["mean"]+monthly["std"],
    alpha=0.3
)
ax.tick_params(axis="x",rotation=45)
ax.set_title("monthly high score")
ax.legend()
plt.show()
