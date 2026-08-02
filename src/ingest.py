from pyspark.sql import SparkSession
from config import ORDERS_CSV, APP_NAME
from schema import orders_schema
from validation import validate_orders

def main():

    """Run the Orders ingestion and validation pipeline."""

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

    # Validate the DataFrame
    valid_df, invalid_df, validation_summary = validate_orders(df)

    print("\nValidation Summary")
    print("-------------------")
    print(f"Total Records   : {validation_summary['total_records']}")
    print(f"Valid Records   : {validation_summary['valid_records']}")
    print(f"Invalid Records : {validation_summary['invalid_records']}")

    # Display schema and sample valid records
    print("\nSchema: ")
    valid_df.printSchema()
    print("\nSample data: ")
    valid_df.show(5)
    # Display the invalid records if any
    if validation_summary["invalid_records"] > 0:
        print("\nInvalid Records:")
        invalid_df.show(5)

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()