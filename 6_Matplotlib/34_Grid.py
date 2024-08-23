import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [11,21,31,41,51]

'''Basic plot code'''
# plt.plot(x, color='green', label='For x')
# plt.plot(y, color='red', label='For y')

# plt.xlabel('x-axis')
# plt.ylabel('y-axis')

# plt.title('Basic lines')
# plt.legend()

'''subplots() method'''
fig, (ax1, ax2) = plt.subplots(1, 2)  # Corrected usage

ax1.plot(x, y)
ax1.grid(True)

ax2.plot(x, [i**2 for i in y])
ax2.grid(True)

'''Grid() method to add grid'''
# plt.plot(x)
# plt.plot(y)
# plt.grid(True, color='grey', linestyle='--', linewidth=0.5)

plt.show()