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
from logger import logger

def main():
    """Run the Orders transformation pipeline."""

    try:
        spark = None

        logger.info("Starting Silver pipeline for Orders")

        # Create Spark session
        spark = (
            SparkSession.builder
            .appName(APP_NAME)
            .getOrCreate()
        )

        # Read Bronze Parquet
        logger.info("Reading Bronze Parquet from %s", BRONZE_ORDERS_DIR)
        bronze_df = spark.read.parquet(str(BRONZE_ORDERS_DIR))

        # Cleanse the data
        logger.info("Cleansing orders")
        cleaned_df, duplicate_count = cleanse_orders(bronze_df)
        logger.info(
            "Business Key: order_id | Duplicates Removed: %s",
            duplicate_count
        )

        # Apply null handling
        logger.info("Applying null handling")
        null_handled_df = handle_nulls(cleaned_df)

        # Apply transformations
        logger.info("Applying transformations")
        silver_df = transform_orders(null_handled_df)

        # Write Silver Parquet
        logger.info("Writing Silver Parquet to %s", SILVER_ORDERS_DIR)
        write_parquet(silver_df, SILVER_ORDERS_DIR)

        # Verify output
        logger.info("Verifying Silver Parquet output")
        verified_df = spark.read.parquet(str(SILVER_ORDERS_DIR))
        verified_df.printSchema()
        verified_df.show(5, truncate=False)
        logger.info("Silver record count: %s", verified_df.count())
        logger.info("Silver pipeline for Orders completed successfully.")

    except Exception as e:
        logger.exception("Silver pipeline failed")
    finally:
        if spark is not None:
            spark.stop()


if __name__ == "__main__":
    main()