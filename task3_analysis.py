import os
import pandas as pd
import numpy as np

# -------------------------------
# STEP 1: AUTO FIND CSV FILE
# -------------------------------
data_folder = "data"

files = os.listdir(data_folder)
csv_files = [f for f in files if f.endswith(".csv")]

if not csv_files:
    print("No CSV file found in data folder!")
    exit()

# Pick the cleaned CSV (prefer trends_clean.csv if exists)
file_name = None
for f in csv_files:
    if "clean" in f:
        file_name = f
        break

# If not found, take first CSV
if not file_name:
    file_name = csv_files[0]

file_path = os.path.join(data_folder, file_name)

print(f"Loading file: {file_path}")

# -------------------------------
# STEP 2: LOAD DATA
# -------------------------------
df = pd.read_csv(file_path)

print(f"\nLoaded data shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

# -------------------------------
# STEP 3: ANALYSIS (NumPy)
# -------------------------------

avg_score = np.mean(df["score"])
avg_comments = np.mean(df["num_comments"])

print("\nAverage score:", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))

# Detailed stats
print("\n--- NumPy Stats ---")
print("Mean score:", np.mean(df["score"]))
print("Median score:", np.median(df["score"]))
print("Std deviation:", round(np.std(df["score"]), 2))
print("Max score:", np.max(df["score"]))
print("Min score:", np.min(df["score"]))

# Category with most stories
most_category = df["category"].value_counts().idxmax()
print("\nMost stories category:", most_category)

# Most commented story
top_story = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:", top_story["title"], "-", top_story["num_comments"], "comments")

# -------------------------------
# STEP 4: ADD NEW COLUMNS
# -------------------------------

# Engagement formula
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular flag
df["is_popular"] = df["score"] > avg_score

# -------------------------------
# STEP 5: SAVE RESULT
# -------------------------------
output_path = os.path.join(data_folder, "trends_analysed.csv")

df.to_csv(output_path, index=False)

print(f"\nSaved analysed data to: {output_path}")
