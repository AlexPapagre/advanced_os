import os

import matplotlib.pyplot as plt
import pandas as pd

# Step 0: Setup
output_folder = "outputs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 1: Load dataset
df = pd.read_csv(
    "data/horse_racing.csv", dtype={"sex_rest": "category"}, low_memory=False
)

# Step 2: Cleaning data
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["pos"] = df["pos"].astype(str)

# Step 3: Running analytics
race_counts = df["course"].value_counts()
avg_age = df.groupby("course")["age"].mean()
position_counts = df["pos"].value_counts()

# Step 4: Generating plots
plt.figure(figsize=(8, 5))
race_counts.head(15).plot(kind="bar", color="skyblue")
plt.title("Number of Horses per Course")
plt.ylabel("Count")
plt.xlabel("Course")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "races_per_course.png"))
plt.close()

plt.figure(figsize=(8, 5))
avg_age.head(15).plot(kind="bar", color="salmon")
plt.title("Average Age of Horses per Course")
plt.ylabel("Average Age")
plt.xlabel("Course")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "avg_age_per_course.png"))
plt.close()

# Step 5: Writing results
with open(os.path.join(output_folder, "analytics_results.txt"), "w") as f:
    f.write("=== Horse Racing Analytics ===\n\n")

    f.write("Number of horses per course:\n")
    f.write(race_counts.to_string())

    f.write("\n\nAverage age of horses per course:\n")
    f.write(avg_age.round(2).to_string())

    f.write("\n\nNumber of horses per finishing position:\n")
    f.write(position_counts.to_string())
