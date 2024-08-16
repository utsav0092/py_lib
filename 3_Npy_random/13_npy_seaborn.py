"""pip install seaborn"""

import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot([0,1,2,3,4,5]) #with histogram
sns.distplot([0,1,2,3,4,5], hist=False) #without histogram
plt.show()