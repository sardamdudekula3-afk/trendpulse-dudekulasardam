import os
import pandas as pd

# -------------------------------
# STEP 1: AUTO FIND JSON FILE
# -------------------------------
data_folder = "data"

# Get all JSON files in data folder
files = os.listdir(data_folder)
json_files = [f for f in files if f.endswith(".json")]

if not json_files:
    print("No JSON file found in data folder!")
    exit()

# Pick the first JSON file (your Task 1 output)
file_path = os.path.join(data_folder, json_files[0])

print(f"Loading file: {file_path}")

# -------------------------------
# STEP 2: LOAD JSON INTO DATAFRAME
# -------------------------------
df = pd.read_json(file_path)

print(f"Loaded {len(df)} rows")

# -------------------------------
# STEP 3: CLEAN THE DATA
# -------------------------------

# 1. Remove duplicates (based on post_id)
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# 2. Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# 3. Fix data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# 4. Remove low quality (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# 5. Remove extra spaces in title
df["title"] = df["title"].str.strip()

# -------------------------------
# STEP 4: SAVE AS CSV
# -------------------------------
output_path = os.path.join(data_folder, "trends_clean.csv")

df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")

# -------------------------------
# STEP 5: SUMMARY
# -------------------------------
print("\nStories per category:")
print(df["category"].value_counts())
