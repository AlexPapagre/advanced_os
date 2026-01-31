import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Step 0: Setup
output_folder = "/opt/outputs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

spark = SparkSession.builder.appName("Horse Racing Analytics").getOrCreate()


def write_and_print(f, text):
    f.write(text)
    print(text, end="")


# Step 1: Load dataset
df = spark.read.csv("/opt/data/horse_racing.csv", header=True, inferSchema=True)

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

# Step 4: Writing results
with open(os.path.join(output_folder, "analytics_results.txt"), "w") as f:
    write_and_print(f, "=== Horse Racing Analytics ===\n\n")

    write_and_print(f, "Number of horses per course:\n")
    for row in race_counts.collect():
        write_and_print(f, f"{row['course']}: {row['count']}\n")

    write_and_print(f, "\nAverage age of horses per course:\n")
    for row in avg_age.collect():
        write_and_print(
            f,
            f"{row['course']}: {round(row['avg_age'], 2) if row['avg_age'] else 'NA'}\n",
        )

    write_and_print(f, "\nNumber of horses per finishing position:\n")
    for row in position_counts.collect():
        write_and_print(f, f"{row['pos']}: {row['count']}\n")

spark.stop()
