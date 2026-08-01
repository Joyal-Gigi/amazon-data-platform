from pyspark.sql import SparkSession
from config import ORDERS_CSV, APP_NAME
from schema import orders_schema

def main():
    # Initialize Spark session
    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .getOrCreate()
    )

    # Read the orders CSV file into a DataFrame
    df = spark.read.csv(
        str(ORDERS_CSV),
        header=True,
        schema=orders_schema
    )

    # Display the number of rows, schema, and sample data
    print(f"\nNumber of rows: {df.count()}")
    print("\nSchema: ")
    df.printSchema()
    print("\nSample data: ")
    df.show(5)

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()