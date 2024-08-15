"""Numpy Array Slicing"""

import numpy as np

'''Slicing for normal array'''
arr = np.array([0,1,2,3,4,5,6,7,8,9])
slice_result = arr[2:6]
slice_result_three = arr[1:9:2]
print(f"First slicing with two indexs : {slice_result}")
print(f"Second sliciing with three indexs : {slice_result_three}")

'''Slicing for 2D array'''
arr_2d = np.array([[1,2 ,3 ,4],
                   [5,6 ,7 ,8],
                   [9,10,11,12]])
slice_result_2d = arr_2d[0:2,1:3]
print(f"After slicing : {slice_result_2d}")