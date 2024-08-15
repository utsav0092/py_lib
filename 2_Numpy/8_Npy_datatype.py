import numpy as np

'''Normally It will also change the original array'''
# arr = [1,2,3,4,5]
# newarr = arr
# print(newarr)
# newarr[0] = 100
# print(newarr)
# print(arr)
'''To avoid this we can use copy()'''
# arr = [1,2,3,4,5]
# newarr = arr.copy()
# print(newarr)
# newarr[0] = 100
# print(newarr)
# print(arr)

'''With copy()'''
# original_array = np.array([1,2,3,4,5])
# copy_array = original_array.copy()
# copy_array[0] = 100
# print(f"Original array : {original_array}")
# print(f"Copy array : {copy_array}")

# '''With view()'''
# array_view = original_array.view()
# array_view[0] = 99
# print(f"Original array : {original_array}")
# print(f"Copy array view : {array_view}")

'''With 2D array, view() & shape()'''
original_array_2d = np.array([[1,2,3],[4,5,6]])
copy_array_2d = original_array_2d.view()
copy_array_2d.shape = (3,2) # 3 row 2 col
print(f"2d original : {original_array_2d}") 
print(f"copy view: {copy_array_2d}") 