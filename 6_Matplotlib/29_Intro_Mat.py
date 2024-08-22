import matplotlib.pyplot as plt

'''Line ploting'''
x = [-2,-1,0,1,2]
y = [4,1,0,1,4]
plt.plot(x,y)
plt.show()

'''Customized line plot'''
plt.plot(x, y, marker='o', linestyle='--', color='green', label='My Line')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Customized line plot')
plt.legend()
plt.show()