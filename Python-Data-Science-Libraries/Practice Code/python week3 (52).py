# numpy indexing,slicing &strides
import numpy as np
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])

#20 (row 0,col 1)
print(arr[0,1])
#90 (row 2,col 2)
print(arr[2,2])

# 80 (last row,2nd colum)
print(arr[-1,-2])

# 10(first row,first column)
print(arr[-3,-3])

#genral form:arr[start:stop:step]

# rows 0-1,col 1-2
print(arr[0:2,1:3])
 # every second row and every second column
print(arr[::2,::2])

# making slice #view not a copy it cang change original array value part
slice_arr=arr[0,:2]
slice_arr[0]=999
print(arr[0])
# print(arr)


# we make copy to not change original array value
copy_arr=arr[1].copy()
copy_arr[0]=555
# print(copy_arr[0])
print(arr[1])


