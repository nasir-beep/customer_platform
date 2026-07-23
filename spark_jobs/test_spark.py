from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Customer Analytics Platform")
    .master("spark://spark-master:7077")
    .getOrCreate()
)

print("=" * 60)
print("Spark Version:", spark.version)
print("Application Name:", spark.sparkContext.appName)
print("=" * 60)

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Carol", 27),
]

df = spark.createDataFrame(data, ["name", "age"])

df.show()

spark.stop()