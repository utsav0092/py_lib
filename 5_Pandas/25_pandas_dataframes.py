import pandas as pd

'''With dictionary of lists'''
data_dict = dict(
            {'Name' : ['Alice', 'Bob', 'Charlie'],
             'Age' : [25, 30, 43],
             'City' : ['New York', 'England', 'Sydney'],
             'Country' : ['USA', 'UK', 'Australia'],}
             )

data_frame = pd.DataFrame(data_dict)

'''With list of dictionarys'''
data_list_of_dict = list(
                    [{'name':'David','age':25,'city':'Tokyo'},
                     {'name':'Eva','age':20,'city':'Kyoto'}]
                     )

df_from_list_of_dict = pd.DataFrame(data_list_of_dict)

print("Data frame from dictionary : ")
print(data_frame)
print("\n")
print("Data frme from list : ")
print(df_from_list_of_dict)