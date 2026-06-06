# import and export -CSV,excel and JSON
# reading CSV:pd.read_csv()
# parse_dates=['column']-->convert date columns
# usecols=[...]-->load specific column
# nrows=100-->convert subset to save memory
# reading excel:pd.read_excel ('file.xlsx',sheet_name='sheet1')
# reading JSON:pd.read_json('file.json')

# exporting Dataframes:df.to_csv('file.csv',index=False)
# df.to_excel('file.xlsx',index=False)
# df.to_json('file.json',oreint=False)
# memory tips:
# use dtype to specify column types

# key point:
# use parse_dates when working with date/time data

# exporting :csv,excel,json---> easy sharing and interperabilityfor large datasets,load
# only needed columns rows and column

import pandas as pd
import openpyxl
df=pd.read_csv(
    "IPL.csv",
    # convert date  column to datetime mtlb ab usy column nahi smjega balke date smjega
    parse_dates=["date"],
    dtype={
        "venue": "category",
        "match_winner": "category"
    }

)
df.info()

# # # remove invalid rows
clean_df=df[df["margin"]>50]
# clean_df = df[df["team1"] != "Mumbai"]
subset=clean_df[["date","venue","margin","match_winner"]]


subset.to_excel("subset_ipl.xlsx",sheet_name='sales')
subset.to_json("subset_ipl.json",
               orient="records",

               # iso mean internationa organization standard time hy
               date_format="iso")
print("files exported!")
subset.info()