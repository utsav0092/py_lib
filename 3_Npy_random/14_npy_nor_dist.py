"""Numpy Normal Distribution or Gaussian distrubution"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''normal code'''
# num = random.normal(loc=1, scale=2, size=(2,3))
# print(num)

'''with sns and plt provide bell curve graph'''
sns.distplot(random.normal(size=100), hist=False)
plt.show()