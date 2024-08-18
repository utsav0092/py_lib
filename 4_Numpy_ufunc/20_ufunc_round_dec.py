"""Numpy ufunc Rounding Decimals"""

import numpy as np

decimal_array = np.array([3.14159, 2.1765, 1.4234, 4.7865])

'''Decimal values'''
rounded_array = np.round(decimal_array, decimals=2)
print(rounded_array)

'''Rounded values'''
around_result = np.around(decimal_array, decimals=1)
print(around_result)