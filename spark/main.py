import os

import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Step 0: Setup
output_folder = "outputs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

spark = SparkSession.builder.appName("Horse Racing Analytics").getOrCreate()

# Step 1: Load dataset
df = spark.read.csv("data/horse_racing.csv", header=True, inferSchema=True)

# Step 2: Cleaning data
df = df.withColumn("age", col("age").cast("double")).withColumn(
    "pos", col("pos").cast("string")
)

# Step 3: Running analytics
race_counts = df.groupBy("course").count().orderBy(col("count").desc())

avg_age = (
    df.groupBy("course").agg(avg("age").alias("avg_age")).orderBy(col("avg_age").desc())
)

position_counts = df.groupBy("pos").count().orderBy(col("count").desc())

# Step 4: Generating plots
race_counts_pd = race_counts.limit(15).toPandas()
avg_age_pd = avg_age.limit(15).toPandas()

plt.figure(figsize=(8, 5))
plt.bar(race_counts_pd["course"], race_counts_pd["count"])
plt.title("Number of Horses per Course")
plt.ylabel("Count")
plt.xlabel("Course")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "races_per_course.png"))
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(avg_age_pd["course"], avg_age_pd["avg_age"])
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
    for row in race_counts.collect():
        f.write(f"{row['course']}: {row['count']}\n")

    f.write("\nAverage age of horses per course:\n")
    for row in avg_age.collect():
        f.write(
            f"{row['course']}: {round(row['avg_age'], 2) if row['avg_age'] else 'NA'}\n"
        )

    f.write("\nNumber of horses per finishing position:\n")
    for row in position_counts.collect():
        f.write(f"{row['pos']}: {row['count']}\n")

spark.stop()
