import numpy as np

'''suffle() to suffle the array'''
original_array = np.array([1,2,3,4,5,6])
np.random.shuffle(original_array)
print(f"Suffled array : {original_array}")

'''permutation() for the array'''
original_array_two = np.array([1,2,3,4,5,6])
permuted_array = np.random.permutation(original_array_two)
print(f"Permuted array : {permuted_array}")

'''2D array with permutation()'''
original_array_two_D = np.array([[1,2,3],[4,5,6],[7,8,9]])
Permuted_row = np.random.permutation(original_array_two_D)
Permuted_col = np.random.permutation(original_array_two_D.T).T
print(f"Permuted array row : {Permuted_row}")
print(f"Permuted array col : {Permuted_col}")