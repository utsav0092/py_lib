from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''console output'''
x = random.uniform(size=(2,3))
print(x)

'''graphical output'''
sns.distplot(random.uniform(size=(1000)), hist=False)
plt.show()