from scipy import constants, special
import numpy as np

'''For checking the version'''
# print("Scipy Version: ", scipy.__version__)

'''Basic maths operation with the scipy'''
result_add = np.add(5,3)
result_exp = np.exp(2)
result_bassel = special.jn(2,3)

print(f"Add : {result_add}")
print(f"Exponential function : {result_exp}")
print(f"Bassel function : {result_bassel}")