import numpy as np
from scipy.stats import ttest_ind, kstest, describe

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

# res = ttest_ind(v1, v2)

# res = kstest(v1, 'norm')

res = describe(v1)
print(res)