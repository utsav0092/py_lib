import matplotlib.pyplot as plt
import numpy as np

y = np.array([34,21,23,65])
mylabels = ["apple","banana","orange","mangos"]
plt.pie(y, labels=mylabels, startangle=90)
plt.legend()

plt.show()