import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Step 0: Setup
DATA_PATH = "/opt/data/horse_racing.csv"
OUTPUT_DIR = "/opt/outputs"
ANALYTICS_FILE = os.path.join(OUTPUT_DIR, "analytics_results.txt")

LM_STDUIO_URL = ""
MODEL_NAME = "mistral-7b-instruct"
LLM_SUMMARY_FILE = os.path.join(OUTPUT_DIR, "llm_summary.txt")


os.makedirs(OUTPUT_DIR, exist_ok=True)

spark = SparkSession.builder.appName("Horse Racing Analytics").getOrCreate()


def write_and_print(f, text):
    f.write(text)
    print(text, end="")


# Step 1: Load dataset
df = spark.read.csv(DATA_PATH, header=True, inferSchema=True)

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
with open(ANALYTICS_FILE, "w") as f:
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

# Step 5: Send output to offline LLM
with open(ANALYTICS_FILE, "r") as f:
    analytics_text = f.read()

prompt = f"""
1234

Analytics output:
{analytics_text}
"""

summary = ""

# Step 6: Save LLM summary
with open(LLM_SUMMARY_FILE, "w") as f:
    f.write(summary)

print("\n=== LLM Summary ===\n")
print(summary)
print("\n")

spark.stop()
