import matplotlib.pyplot as plt

categories = ['Categories A','Categories B','Categories C','Categories D']
values = [12,23,45,21]

plt.bar(categories, values, color=['orange','pink','skyblue','gray'], edgecolor='black')
plt.title('Bars plot')
plt.xlabel('Values')
plt.ylabel('Categories')

plt.show()