import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analysis.csv")

plt.bar(df["category"], df["views"])
plt.xlabel("Category")
plt.ylabel("Views")
plt.title("Trend Analysis")

plt.show()
