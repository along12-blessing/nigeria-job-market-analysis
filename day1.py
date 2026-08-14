import pandas as pd

df = pd.read_json('houses.json')


print(df.to_string())

print(df.isnull().sum())
