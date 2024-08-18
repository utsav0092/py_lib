"""Python numpy universal library"""

import numpy as np

def myadd(x, y):
    return x + y
myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1,2,3,4],[5,6,7,8]))
print(type(np.add))

'''To check'''

if type(np.add) == np.ufunc:
    print(f"add is ufunc")
else:
    print(f"add is not ufunc")