import numpy as np
from scipy.spatial import Delaunay, ConvexHull
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

points = np.array([
    [2, 4],
    [4, 5],
    [3, 4],
    [3, 2],
    [4, 1],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2],
])

# simplices = Delaunay(points).simplices

hull = ConvexHull(points)
hull_points = hull.simplices

# plt.triplot(points[:, 0], points[:, 1], simplices)
# plt.scatter(points[:, 0], points[:, 1], color='red')

plt.scatter(points[:, 0], points[:, 1])
for simplex in hull_points:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.show()

points = [(1,-1),(2,3),(-2,3),(2,-3)]

kdtree = KDTree(points)
res = kdtree.query((1,1))
print(res)