import numpy as np

data_array = np.array([1,2,3,4,5])
array = np.array([5,6,7,8,9])

'''Product method'''
try:
    result = np.prod(data_array)
    print(f"Product result : {result}")

    axis_prod_result = np.prod((data_array), axis=0)
    print(f"With axis : {axis_prod_result}")

    new_array = np.cumprod(array)
    print(f"Cummulative product : {new_array}")
except:
    print("IncorrectMethodCall")