from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    upper,
    trim,
    concat_ws,
    count,
    when
)

# ----------------------------
# Create Spark Session
# ----------------------------
spark = (
    SparkSession.builder
    .appName("Customer ETL")
    .getOrCreate()
)

# ----------------------------
# Read Customer Dataset
# ----------------------------
df = spark.read.csv(
    "data/raw/crm_50000_customers_dirty_v3.csv",
    header=True,
    inferSchema=True
)

print("\nFirst 5 Rows")
df.show(5)

print("\nSchema")
df.printSchema()

print(f"\nTotal Records: {df.count()}")

# ----------------------------
# Missing Values
# ----------------------------
print("\nMissing Values")

missing = df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in df.columns
])

missing.show()

# ----------------------------
# Remove Duplicate Customers
# ----------------------------
before = df.count()

df = df.dropDuplicates(["customer_id"])

after = df.count()

print(f"Duplicates Removed: {before - after}")

# ----------------------------
# Remove Invalid Records
# ----------------------------
df = df.dropna(
    subset=[
        "customer_id",
        "email"
    ]
)

# ----------------------------
# Standardize Text
# ----------------------------
df = (
    df
    .withColumn("country", upper(trim(col("country"))))
    .withColumn("city", upper(trim(col("city"))))
    .withColumn("state", upper(trim(col("state"))))
)

# ----------------------------
# Create Full Name
# ----------------------------
df = df.withColumn(
    "full_name",
    concat_ws(
        " ",
        trim(col("first_name")),
        trim(col("last_name"))
    )
)

print("\nCleaned Data")

df.show(5)

# ----------------------------
# Save Cleaned Dataset
# ----------------------------
(
    df.write
    .mode("overwrite")
    .option("header", True)
    .csv("data/processed/customers")
)

print("\nCustomer ETL Completed Successfully!")

spark.stop()