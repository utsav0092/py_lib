import matplotlib.pyplot as plt

one = [2,4,5,7,8]
two = [10,15,20,25,30]

'''Basic scatter method'''
# plt.scatter(one,two)

'''Customized scatter method'''
# plt.scatter(one,two, color='red', marker='o', s=100, edgecolors='black')
plt.title('Scatter graph')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()