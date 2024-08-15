import numpy as np

'''Create 1D array'''
your_arr = np.array([1, 2, 3, 4, 5])
print(f"1D array : {your_arr}")

'''Create 2D array'''
my_arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array : {my_arr}")

'''Create 3D array'''
our_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"3D array : {our_arr}")

their_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(f"New array : {their_arr}")

whose_arr = np.array([1, 2, 3, 4], ndmin=5)
print(f"With ndmin : {whose_arr}")
print(f"Number of dimensions : {whose_arr.ndim}")
