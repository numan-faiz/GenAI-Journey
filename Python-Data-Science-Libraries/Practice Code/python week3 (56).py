# pandas indexing and selection / .loc and .iloc
# we see in pandas that how to access and change the subset of data
#sample dataframe
import pandas as pd

data={
    'name':['numan','jusa','suda','boda'],
    'age':[2,3,4,5],
    'city':['nigeria','sudan','butan','kutan'],
    'salary':[344444,56666,78886,75543]
}
df=pd.DataFrame(data)
print(df)


# 1# label-based selection using .loc
# include starting and ending both
subset_loc=df.loc[1:3, ['name','salary']]
print("the subset of .location is :", subset_loc)

#2 integer -based selection
 # include 0 and 1 include starting and 2 3 not include ending
subset_iloc=df.iloc[0:2,1:3]
print("the subset ilocation is : \n ",subset_iloc)


#boolean filtering


high_salary=df[df['salary']>75000]
print("the highest salary is: \n",high_salary)


# 4#safe assighment using .loc is used to assign data to data subset or data frame
df.loc[df['age']<30,'salary']=65000
print("low age salary is :\n",df.loc[df['age']<30,'salary'])




