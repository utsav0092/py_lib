"""Python ufunc Summation"""

import numpy as np

data_array = np.array([10, 20, 30, 40, 50])

result = np.sum(data_array)
print(f"Summation of the array : {result}")

axis_sum_resutl = np.sum(data_array, axis=0)
print(f"Axis sum : {axis_sum_resutl}")

'''Cummulative summation'''
arr = np.array([1,2,3,4,5])
newarr = np.cumsum(arr)
print(newarr)