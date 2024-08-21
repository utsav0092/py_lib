import pandas as pd

file_path = 'data.csv'
df = pd.read_csv(file_path)

print("Dataframe of csv file : ")
print(df)

print(f"Value : {pd.options.display.max_rows}")
pd.options.display.max_rows = 100

df = pd.read_csv('data.csv')
print(df)