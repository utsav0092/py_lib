import numpy as np
from scipy.sparse import csr_matrix

# dense_matrix = np.array([[1,0,0],[0,0,2],[3,0,4]])

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])

# sparse_matrix = csr_matrix(dense_matrix)

# print("dense matrix")
# print(dense_matrix)
# print("\nSparse matrix")
# print(sparse_matrix)

# print(csr_matrix(arr).data)

# print(csr_matrix(arr).count_nonzero())

# mat = csr_matrix(arr)
# mat.eliminate_zeros()
# mat.sum_duplicates()
# print(mat)

newarr = csr_matrix(arr).tocsc()
print(newarr)