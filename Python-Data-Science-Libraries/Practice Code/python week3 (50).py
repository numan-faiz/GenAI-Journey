# why  numpy and environment setup
# pure python lists are slow & memory-inefficient
# numpy provide ndarray(n-dimensional array)
# enables fast numerical operations(vectorized
# forms the foundation for scientific computing & Ml libraries)
import time

# key concepts:
# ndarray-->core data structure
# Shape--->dimension of the array(rows*column)
# ndim--->number of dimension:(1D,2D,3D,....
# dtype--->DATATYPE OF THE ARRAY elements(int,float,etc)
# pip install numpy--->for installation


# .\.venv\Scripts\activate---> activate virtual enviroment agar hmry passs pakges install hoke kam
# na krein

import numpy as np
arr=np.array([[1,2,3],[3,7,9]])
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

my_list=list(range(1000000))
py_result=[]
start_time=time.time()
for i in my_list:
    py_result.append(i+5)
end_time=time.time()
print("python list time is",end_time-start_time)

np_array=np.arange(1000000)
start_time=time.time()
result_array=np_array+5
end_time=time.time()
print("numpy array time is",end_time-start_time)

