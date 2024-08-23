import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
y2 = [21,41,61,18,10]

plt.plot(x, color='green', label='For X', marker='o')
plt.plot(y, color='red', label='For Y', marker='o')
plt.plot(y2, color='blue', label='For Y2', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Labeled plot')

'''Basic legend() method'''
## Essential when plotting for the multiple data series
# plt.legend() 

'''Customized legend() method'''
plt.legend(loc='upper left', fontsize=12, frameon=False)

plt.show()