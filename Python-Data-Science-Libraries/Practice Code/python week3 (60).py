# string and text cleaning in pandas

import pandas as pd
df=pd.DataFrame({
    'Category': [' Electronics ','Furniture','Home-Appliances',' electronics', 'FURNITURE ']

})
print(df)


#strip spaces and convert to lowercase
df['Category_clean']=df['Category'].str.strip().str.lower()
print(df)


#replace hypens with space
df['Category_clean']=df['Category_clean'].str.replace('-', ' ')
print(df)



