# merging and joining data frames
# methods of joining
# inner join
# outer join
# left join
# right join

import pandas as pd
customer=pd.DataFrame({
    'customerID':[1,2,3],
    'name':['alice','bob','charlie']

})
orders=pd.DataFrame({
    'orderid':[101,102,103,104],
    'customerID':[1,2,2,4],
    'amount':[150,250,150,300],
})

# print(customer,orders)
df_inner=pd.merge(customer,orders, on='customerID',how='inner')
print(df_inner)

df_left=pd.merge(customer,orders, on='customerID',how='left')
print(df_left)
df_right=pd.merge(customer,orders, on='customerID',how='right')
print(df_right)
df_outer=pd.merge(customer,orders, on='customerID',how='outer')
print(df_outer)


# concate-rows example
df_concat=pd.concat([customer,customer])
print("concate rows\n: ",df_concat)
