import numpy as np
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order
from scipy.sparse import csr_matrix

# arr = np.array([
#     [0, 1, 2],
#     [1, 0, 0],
#     [2, 0, 0]
# ])

# arrtwo = np.array([
#     [0, -1, 2],
#     [1, 0, 0],
#     [2, 0, 0]
# ])

arrthree = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [0, 1, 0, 1]
])

# new_arr = csr_matrix(arr)
# arrtwo = csr_matrix(arr)
arrthree = csr_matrix(arrthree)

# Uncomment the following line if you want to check the connected components
# print(connected_components(new_arr))

# Use dijkstra to find the shortest paths

# dist_matrix, predecessors = dijkstra(new_arr, return_predecessors=True, indices=0)
# print("Distance Matrix:\n", dist_matrix)
# print("Predecessors:\n", predecessors)

# print(floyd_warshall(new_arr, return_predecessors=True))

# print(bellman_ford(arrtwo, return_predecessors=True, indices=0))

# print(depth_first_order(arrthree, 1))

print(breadth_first_order(arrthree, 1))