from config import RAW_DATA, PROCESSED_DATA
from logger import get_logger
from quality import (
    remove_duplicates,
    remove_null_ids,
    count_rows,
)
from utils import create_spark_session

logger = get_logger("customers")

spark = create_spark_session("Customer ETL")

logger.info("Reading customer dataset...")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(str(RAW_DATA / "crm_50000_customers_dirty_v3.csv"))
)

logger.info(f"Rows before cleaning: {count_rows(df)}")

df = remove_duplicates(df)

df = remove_null_ids(df, "customer_id")

logger.info(f"Rows after cleaning: {count_rows(df)}")

(
    df.write
    .mode("overwrite")
    .option("header", True)
    .csv(str(PROCESSED_DATA / "customers"))
)

logger.info("Customer dataset cleaned successfully.")

spark.stop()