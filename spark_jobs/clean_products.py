from pyspark.sql.functions import col

from config import RAW_DATA, PROCESSED_DATA
from logger import get_logger
from quality import (
    remove_duplicates,
    remove_null_ids,
    count_rows,
)
from utils import create_spark_session

logger = get_logger("products")

spark = create_spark_session("Product ETL")

logger.info("Reading product dataset...")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(str(RAW_DATA / "product_catalog_dirty_30pct.csv"))
)

logger.info(f"Rows before cleaning: {count_rows(df)}")

df = remove_duplicates(df)

df = remove_null_ids(df, "product_id")

# Remove products with invalid prices
df = df.filter(col("price") > 0)

logger.info(f"Rows after cleaning: {count_rows(df)}")

(
    df.write
    .mode("overwrite")
    .option("header", True)
    .csv(str(PROCESSED_DATA / "products"))
)

logger.info("Product dataset cleaned successfully.")

spark.stop()