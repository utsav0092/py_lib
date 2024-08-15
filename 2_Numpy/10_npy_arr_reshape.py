import numpy as np

'''Reshping the array using (.reshape) method'''
original_array = np.array([1,2,3,4,5,6])
reshaped_array = original_array.reshape(2,3)
print(f"Original array : {original_array}")
print(f"Reshaped array : {reshaped_array}")

'''With majors'''
original_array = np.array([1,2,3,4,5,6])
row_major = original_array.reshape(2,3, order='C')
col_major = original_array.reshape(2,3, order='F')
print(f"Original array : {original_array}")
print(f"row major array : {row_major}")
print(f"col major array : {col_major}")