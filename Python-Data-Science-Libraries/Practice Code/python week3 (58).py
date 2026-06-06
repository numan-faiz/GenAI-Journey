# handling data types and type conversion
import pandas as pd

df=pd.read_csv(
    "IPL.csv",
    # convert date column to determine
    parse_dates=["date"],
    dtype={
    "venue":"category"
}
)
print(df.info)

# convert column  to numeric

df['margin']=pd.to_numeric(df['margin'])
print(df.info())


# convert column into category
df['top_scorer']=df['top_scorer'].astype('category')
print(df.info)

# use to check data usage
print(df['top_scorer'].memory_usage(deep=True))



























