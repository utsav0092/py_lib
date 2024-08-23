import matplotlib.pyplot as plt
import numpy as np

'''Basic example'''
ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o')
plt.show()

'''Other markers'''
x = [1,2,3,4,5]
y = [10,15,30,25,35]
plt.plot(x, marker = 'o', label='Circle')
plt.plot(x, marker = 's', label='Square')
plt.plot(x, y, marker = '^', label='Triangle')
plt.plot(x, y, marker = '*', label='Start')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Basic marker types')
plt.legend()
plt.show()