import numpy as np

'''Shape of the array using (.shape) method returns (no.rows, no.cols)'''
arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],
                   [4,5,6]])
arr_3d = np.array([[[1,2],
                    [3,4],
                    [5,6],
                    [7,8]]])

print(f"Shape of 1D array : {arr_1d.shape}")
print(f"Shape of 2D array : {arr_2d.shape}")
print(f"Shape of 3D array : {arr_3d.shape}")

'''ndmin = dimension of array'''
arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print(f"Shape of array : {arr.shape}")