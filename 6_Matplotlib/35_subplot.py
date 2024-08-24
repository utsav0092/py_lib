import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.plot([1,2,3],[4,5,6])
plt.title('Plot 1')

plt.subplot(2,2,2)
plt.plot([3,2,1],[6,5,4])
plt.title('Plot 2')

plt.subplot(2,2,3)
plt.plot([1,2,3],[4,5,6], color='red')
plt.title('Red plot')

plt.subplot(2,2,4)
plt.plot([3,2,1],[6,5,4], color='purple')
plt.title('Purple plot')

plt.show()