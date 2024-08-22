import pandas as pd

'''From json file'''
file_path = 'team.json'
df = pd.read_json(file_path)
print(df)

'''Dictionary dataframe'''
data = {
    "Duration":{
        "0":60,
        "1":59,
        "2":60,
        "3":45,
    },
    "Purlse":{
        "0":101,
        "1":190,
        "2":120,
        "3":130,
    },
    "Maxpulse":{
        "0":110,
        "1":140,
        "2":123,
        "3":132,
    },
    "Calories":{
        "0":80.8,
        "1":21.9,
        "2":23.6,
        "3":43.7,
    }
}
df = pd.DataFrame(data)
print(df)