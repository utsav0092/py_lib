"""Numpy ufunc simple arithmetic operations"""

import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

'''Addition'''
add_result = np.add(arr1,arr2)
print(f"Addition of arrays : {add_result}")

'''Subtraction'''
sub_result = np.subtract(arr1,arr2)
print(f"Sub of array : {sub_result}")

'''Multiplication'''
mul_result = np.multiply(arr1, arr2)
print(f"Multiplication of arrays : {mul_result}")

'''Divisiion'''
div_result = np.divide(arr1, arr2)
print(f"Divide of arrays : {div_result}")

'''Scaler multiply'''
scaler_multiply = np.multiply(arr1, 2)
print(f"Scaler multiplication of arrays : {scaler_multiply}")