"""Poisson Distribution"""

"""
A Poisson distribution is a discrete probability distribution. 
It gives the probability of an event happening a certain number 
of times (k) within a given interval of time or space. 
The Poisson distribution has only one parameter, λ (lambda), 
which is the mean number of events.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''console output'''
# x = random.poisson(lam=2, size=10)
# print(x)

'''Graph output'''
# sns.displot(random.poisson(lam=2, size=1000), kde=False)
# plt.show()

'''Difference b/w normal and poisson distribution'''
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()