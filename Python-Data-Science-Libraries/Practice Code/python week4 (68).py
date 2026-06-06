# correlation and covraince analysis
# it measure the relationships between numerical vairables if one is incrase other is also increase
# so its positive relation if less both at time still positive corelation

# if one increase other decrese then its negative corelation
# covraince tell the realtion in absolute unit between dffrnt vraible
# while coreklation tells at percentage between diffrent variable

# it work only on numerical column not work on strings and categorical column
import pandas as pd
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)

numeric_df=df[["price","review_score","review_count","sales_month_2","sales_month_4","sales_month_6",
            "sales_month_8","sales_month_10","sales_month_11","sales_month_12"]]

# covraince matrix
print("cvraince is \n: ",numeric_df.cov())
# correlation matrix
print("corelation is \n",numeric_df.corr())

# focus on relationship in sorting form
print(numeric_df.corr()["price"].sort_values(ascending=False))


 # to find minium corelation and maximun corelation
print(numeric_df.corr().values.min(),numeric_df.corr().values.max())

