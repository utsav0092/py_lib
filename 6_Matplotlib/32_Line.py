import matplotlib.pyplot as plt

x = [1,2,3,4,5]
x2 = [11,21,31,41,51]
y = [10,15,25,30,20]
y2 = [5,10,15,20,25]

plt.plot(x2, label='Line 1')
plt.plot(y2, linestyle='--', color='green', label='New line')

plt.plot(x, label='Data line')
plt.plot(y, linestyle='--', color='red', label='Dashed red line')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
# plt.title('Plotting Line Data')
# plt.title('Line style and color')
plt.title('Multiple line in a single plot')
plt.legend()
plt.show()