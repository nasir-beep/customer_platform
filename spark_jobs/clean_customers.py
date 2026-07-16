from pyspark.sql.functions import col

from config import RAW_DATA, PROCESSED_DATA
from utils import create_spark_session

spark = create_spark_session("Clean Customers")

# Read CSV
df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(str(RAW_DATA / "crm_50000_customers_dirty_v3.csv"))
)

print("\nSchema")
df.printSchema()

print("\nRow Count")
print(df.count())

print("\nFirst Records")
df.show(5)

# Remove duplicates
df = df.dropDuplicates()

# Remove rows without customer_id
df = df.filter(col("customer_id").isNotNull())

# Save cleaned data
(
    df.write
    .mode("overwrite")
    .option("header", True)
    .csv(str(PROCESSED_DATA / "customers"))
)

print("Customer cleaning completed!")

spark.stop()