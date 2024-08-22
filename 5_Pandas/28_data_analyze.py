import pandas as pd

'''Starting with head() to get starting overview'''
df = pd.read_csv('data.csv')
print(df.head(2))
# print(df.head())  #only print upto 5 term

'''With the tail() to get last overview'''
print(df.tail(2))

'''All information about the data wiht info()'''
print(df.info())