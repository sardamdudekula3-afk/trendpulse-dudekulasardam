import os
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: AUTO FIND CSV (Task 3)
# -------------------------------
data_folder = "data"

files = os.listdir(data_folder)
csv_files = [f for f in files if f.endswith(".csv")]

if not csv_files:
    print("No CSV file found!")
    exit()

# Prefer analysed file
file_name = None
for f in csv_files:
    if "analysed" in f:
        file_name = f
        break

# fallback
if not file_name:
    file_name = csv_files[0]

file_path = os.path.join(data_folder, file_name)

print(f"Loading file: {file_path}")

df = pd.read_csv(file_path)

# Create output folder
os.makedirs("outputs", exist_ok=True)

# -------------------------------
# CHART 1: Top 10 stories by score
# -------------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -------------------------------
# CHART 2: Stories per category
# -------------------------------
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Stories per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# -------------------------------
# CHART 3: Score vs Comments
# -------------------------------
plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")

# highlight popular
popular = df[df["is_popular"] == True]
plt.scatter(popular["score"], popular["num_comments"])

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -------------------------------
# BONUS: DASHBOARD
# -------------------------------
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1
axs[0].barh(top10["title"], top10["score"])
axs[0].set_title("Top Stories")
axs[0].invert_yaxis()

# Chart 2
axs[1].bar(category_counts.index, category_counts.values)
axs[1].set_title("Categories")

# Chart 3
axs[2].scatter(df["score"], df["num_comments"])
axs[2].set_title("Score vs Comments")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in 'outputs/' folder")
