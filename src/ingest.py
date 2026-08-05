from pyspark.sql import SparkSession
from config import (
    APP_NAME,
    ORDERS_CSV,
    BRONZE_ORDERS_DIR,
)
from schema import orders_schema
from validation import validate_orders
from writer import write_parquet


def main():
    """Run the Orders ingestion pipeline."""

    # Create Spark session
    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .getOrCreate()
    )

    # Read Orders CSV using explicit schema
    orders_df = (
        spark.read
        .option("header", True)
        .schema(orders_schema)
        .csv(str(ORDERS_CSV))
    )

    # Validate records
    valid_df, invalid_df, summary = validate_orders(orders_df)

    # Validation summary
    print("\nValidation Summary")
    print("-------------------")
    print(f"Total Records   : {summary['total_records']}")
    print(f"Valid Records   : {summary['valid_records']}")
    print(f"Invalid Records : {summary['invalid_records']}")

    # Display schema
    print("\nSchema")
    valid_df.printSchema()

    # Display sample valid records
    print("\nSample Valid Records")
    valid_df.show(5, truncate=False)

    # Display invalid records (if any)
    if summary["invalid_records"] > 0:
        print("\nSample Invalid Records")
        invalid_df.show(5, truncate=False)

    # Write Bronze Parquet
    write_parquet(valid_df, BRONZE_ORDERS_DIR)

    # Verify output
    bronze_df = spark.read.parquet(str(BRONZE_ORDERS_DIR))

    print("\nBronze Layer Verification")
    print("-------------------------")
    print(f"Rows Written : {bronze_df.count()}")

    bronze_df.show(5, truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()