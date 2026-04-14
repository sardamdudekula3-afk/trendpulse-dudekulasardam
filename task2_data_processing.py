import pandas as pd

df = pd.read_json("data.json")
df = df.drop_duplicates()
df.to_csv("clean_data.csv", index=False)

print("Cleaned data saved")
