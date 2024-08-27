# import scipy.io
# import numpy as np

'''Making the collabortion between the MATLAB and python'''
## 1:-
# mat_data = scipy.io.loadmat('matlab_data.mat')

# mat_array = mat_data['myMatArray']

# print("Matlab array in python")
# print(mat_array)

## 2:-
# python_array = np.array([[1,2,3],[4,5,6]])
# scipy.io.savemat('python_data.mat', mdict={'myMatArray': python_array})

'''Data manipulation and analyse with MATLAB'''
# mat_data = scipy.io.loadmat('matlab_data.mat')

# mat_array = mat_data['myMatArray']

# sum_column2 = np.sum(mat_array[:, 1])

# print(f"Sum of the second column : {sum_column2}")