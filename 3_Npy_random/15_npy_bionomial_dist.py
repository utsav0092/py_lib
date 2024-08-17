"""Numpy Binomial Distribution"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''For the binomial distribution'''
n,p,size = 10,0.5,1000
data = np.random.binomial(n,p,size)
count,bins,ignored = plt.hist(data,11,density=True)
plt.show()

'''To show the difference'''
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()