from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Spark Test")
    .getOrCreate()
)
print("Spark Session created successfully.")
print(spark.version)

spark.stop()