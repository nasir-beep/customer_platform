from pyspark.sql.functions import col, to_date

from config import RAW_DATA, PROCESSED_DATA
from logger import get_logger
from quality import (
    remove_duplicates,
    remove_null_ids,
    count_rows,
)
from utils import create_spark_session

logger = get_logger("orders")

spark = create_spark_session("Order ETL")

logger.info("Reading orders dataset...")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(str(RAW_DATA / "orders_300k_dirty.csv"))
)

logger.info(f"Rows before cleaning: {count_rows(df)}")

# Remove duplicate rows
df = remove_duplicates(df)

# Remove rows with missing IDs
df = remove_null_ids(df, "order_id")
df = remove_null_ids(df, "customer_id")
df = remove_null_ids(df, "product_id")

# Keep only positive quantities
df = df.filter(col("quantity") > 0)

# Keep only positive order amounts
df = df.filter(col("order_amount") > 0)

# Convert order_date to Date type
df = df.withColumn(
    "order_date",
    to_date(col("order_date"))
)

logger.info(f"Rows after cleaning: {count_rows(df)}")

(
    df.write
    .mode("overwrite")
    .option("header", True)
    .csv(str(PROCESSED_DATA / "orders"))
)

logger.info("Orders cleaned successfully.")

spark.stop()