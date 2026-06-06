# pandas series and fundamentals
# pandas---->provide to store,arrays and matrices
# series in pandas:--->1D lableled array--->have one label of  data also
# consist of index+values
# automatically  infers dtype

import pandas as pd
# create a series
s=pd.Series([10,20,20,30,40],index=['a','b','c','d','e'])
print(s)
print("values",s.values)
print("index",s.index)
print("dtype",s.dtype)

print(s.head)
print(s.tail)
print(s.value_counts())

