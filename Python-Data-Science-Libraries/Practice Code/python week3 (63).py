# Applying Functions - apply, map & pipe
import pandas as pd

# it is used to manipulate columns and make more columns
df=pd.read_csv(
    "ecommerce_sales_analysis.csv"
)
print(df.info())


# now we use map --->label high value orders and it work on pandas series
df["category_type"]=df["category"].map({

       "Electronic":"Tech",
       "Clothing":"Fashion",
       "Home & Kitchen":"household",
       "Toys":"Kids",
        "Books":"Education"
})
# explanation:each value is mapped/changed and individyually
# for verification of new column
# check unique values

print(df["category_type"].unique())

# compare before vs after
print(df[["category","category_type"]].head())


# check size
print(df.groupby("category_type").size())

# apply()(--->create price category)

def categorize_price(price):
    if price<100:
        return "budget"
    elif price<=3000:
        return "mid range"
    else:
        return "premium"
df["categorize_price"]=df["price"].apply(categorize_price)
print(df["categorize_price"])



# verify check categories
print(df["categorize_price"].value_counts())

# validate logic manually
print(df[["price","categorize_price"]].sample(10))





# pipe()--->method chaining--.by this we till series of sequence to apply on dataset
def round_price(data):
    data["price"]=data["price"].round(1)
    return data
def get_electronics(data):
    return data[data["category"]== "Electronics"]


df2=(
    df.pipe(round_price)
      .pipe(get_electronics)
)
print(df2.head())


