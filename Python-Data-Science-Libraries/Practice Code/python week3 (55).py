# pandas Dataframes-creation and inspection
# its most popular and  in which we import large datasets and use it for ai and Ml
# 2-dimentional labeled data structure in rows and columns
# similar to a spreadsheet or SQL sheet
# can hold diffrenet data types in different classes
# used for data analysis and data manipyulation
import pandas as pd
data={
    'name':['numan','arsal','bonanza'],
    'age':[23,45,67],
    'city':['japan','buzdar','sudan']
}
df=pd.DataFrame(data)
print(df)

#load sample CSV
df=pd.read_csv('IPL.csv')

#insepect dataframe
print("info:\n", df.info())
# print(df)

print("\nshape:",df.shape)
print("\ndata type:\n",df.dtypes)


# its shows the detail of dataset
print("\n statistical summary:\n  ",df.describe())



