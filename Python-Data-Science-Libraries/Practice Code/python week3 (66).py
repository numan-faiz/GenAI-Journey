# Working with Datetime & Time Series Data basics
import pandas as np
import pandas as pd

df=pd.read_csv(
    "IPL.csv",
    parse_dates=["date"]
)
# setting datetime index
df=df.set_index("date")
print(df.index)


# monthly score innings analysis
mothly_score=df["first_ings_wkts"].resample("ME").sum()
print(mothly_score)


# trend interpretatiion mean how much change and write it in percentage
print(mothly_score.pct_change())


# verify that index is monotonically increasing mean is there have any jumps or not
print(mothly_score.index.is_monotonic_increasing)


# ab hm ye dekhngy ke hmra total score ju hy kahi mnthly score usy zyada tu nahi hve
print(mothly_score.sum(),df["first_ings_wkts"].sum())
print(mothly_score.sum() <= df["first_ings_wkts"].sum())
