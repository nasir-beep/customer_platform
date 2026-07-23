from pyspark.sql.functions import trim, col, to_date
from utils import create_spark_session

spark = create_spark_session("Customers ETL")

print("=" * 60)
print("READING CUSTOMERS DATASET")
print("=" * 60)

customers = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/opt/project/data/raw/crm_50000_customers_dirty_v3.csv")
)

print("Rows before cleaning:", customers.count())

customers = customers.dropDuplicates(["customer_id"])

customers = customers.filter(col("customer_id").isNotNull())

string_columns = [
    field.name
    for field in customers.schema.fields
    if field.dataType.simpleString() == "string"
]

for column in string_columns:
    customers = customers.withColumn(column, trim(col(column)))

customers = customers.withColumn(
    "signup_date",
    to_date(col("signup_date"))
)

print("Rows after cleaning:", customers.count())

customers.printSchema()

customers.show(5)

customers.write.mode("overwrite").parquet(
    "/opt/project/data/processed/customers_clean.parquet"
)

print("Customers saved successfully!")

spark.stop()