from pyspark.sql import SparkSession
from cleansing import cleanse_orders
from config import (
    APP_NAME,
    BRONZE_ORDERS_DIR,
    SILVER_ORDERS_DIR,
)
from null_handling import handle_nulls
from transformations import transform_orders
from writer import write_parquet

def main():
    """Run the Orders transformation pipeline."""

    # Create Spark session
    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .getOrCreate()
    )

    # Read Bronze Parquet
    bronze_df = spark.read.parquet(str(BRONZE_ORDERS_DIR))

    #cleanse the data
    cleaned_df = cleanse_orders(bronze_df)

    #apply null handling
    null_handled_df = handle_nulls(cleaned_df)

    # Apply transformations
    silver_df = transform_orders(null_handled_df)

    # Write Silver Parquet
    write_parquet(silver_df, SILVER_ORDERS_DIR)

    # Verify output
    print("\nSilver Layer Verification")
    print("-------------------------")
    verified_df = spark.read.parquet(str(SILVER_ORDERS_DIR))
    verified_df.printSchema()
    verified_df.show(5)
    print(verified_df.count())

    spark.stop()

if __name__ == "__main__":
    main()