from pyspark.sql import SparkSession

# Create a Spark session
spark = (
    SparkSession.builder
    .appName("Hello Spark")
    .getOrCreate()
)

# Create a simple DataFrame
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

columns = ["name", "age"]

df = spark.createDataFrame(data, columns)

print("=== DataFrame ===")
df.show()

print("Total Rows:", df.count())

spark.stop()