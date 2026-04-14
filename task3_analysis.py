import pandas as pd

df = pd.read_csv("clean_data.csv")

result = df.groupby("category")["views"].sum().reset_index()

print(result)
result.to_csv("analysis.csv", index=False)
