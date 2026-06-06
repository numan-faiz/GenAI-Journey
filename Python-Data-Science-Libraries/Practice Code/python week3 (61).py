# sorting and ranking data

import pandas as pd
df=pd.read_csv(
    "IPL.csv",
    parse_dates=["date"],
    dtype={
        "venue":"category",
        "margin":"category"
    }


)
print(df)

# now sort column by ascending and then decending
df_sorted=df.sort_values(by=['first_ings_score','second_ings_score'],ascending=[False,True])
print("sorted DataFrame")
print(df.head())

# now rank score with  groups
df['score-rank']=df.groupby('first_ings_score')['second_ings_score'].rank(method='dense',ascending=False)
print("\n score rank within score group:\n",df )
