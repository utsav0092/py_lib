import pandas as pd

'''Normal example'''
a = [7,5,9]
myvar = pd.Series(a, index=["p","q","r"])
print(myvar)

'''Modified example'''
data_list = [10,20,30,40,50]
series_from_list = pd.Series(data_list)
data_dict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
series_with_index = pd.Series(data_dict)
print("Series from list : ")
print(series_from_list)
print("Series with index : ")
print(series_with_index)