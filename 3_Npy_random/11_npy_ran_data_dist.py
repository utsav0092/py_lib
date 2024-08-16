from numpy import random

'''p = probability of the number sum = 1.0'''
arr = random.choice([3,5,9,7], p=[0.1,0.3,0.4,0.2], size=(10))
print(arr)

'''For 2D array 3 row 5 col'''
arr2d = random.choice([3,5,9,7], p=[0.1,0.3,0.4,0.2], size=(3,5))
print(arr2d)