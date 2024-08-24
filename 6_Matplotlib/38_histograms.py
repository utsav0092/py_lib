import matplotlib.pyplot as plt
import numpy as np

data = [2,3,4,3,5,5,9,6,4,3,3,7]
exam_score = [65,70,55,35,45,90]

plt.hist(exam_score, bins=10, color='skyblue', edgecolor='black')

plt.title('Histogram plot')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.show()

'''for random values'''
# x = np.random.normal(170, 10, 250)
# plt.hist(x, edgecolor='black')
# plt.title('Random plot')

# plt.show()