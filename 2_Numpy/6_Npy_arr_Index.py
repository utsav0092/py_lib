'''Intro to array indexing with Numpy'''
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5])
print(f"fot positive {arr[2]} for negative {arr[-1]}")

'''For 2D array'''
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"positive {arr_2d[1, 2]} for negative {arr_2d[-1, -2]}")

'''Indexing with boolean index'''
arrnew = np.array([1,2,3,4,5,6,7,8,9])
'''Boolean mask for the condition'''
mask = (arrnew > 2)
print(f"Boolean index : {arrnew[mask]}")