"""Numpy log functions"""

import numpy as np

number_array = np.array([1,2,3,4,5])

'''using log()'''
log_result = np.log(number_array)
# print(np.log(number_array))
print(f"log array : {log_result}")

'''Exponential function'''
exp_result = np.exp(number_array)
print(f"Exponential result : {exp_result}") 

'''log ten result'''
log_ten_result = np.log10(number_array)
print(f"log10 result : {log_ten_result}")