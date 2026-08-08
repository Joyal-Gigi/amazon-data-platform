from pyspark.sql import SparkSession
from config import (
    APP_NAME,
    ORDERS_CSV,
    BRONZE_ORDERS_DIR,
)
from schema import orders_schema
from validation import validate_orders
from writer import write_parquet
from logger import logger


def main():
    """Run the Orders ingestion pipeline."""

    try:
        logger.info("Starting Bronze pipeline for Orders")

        spark = None

        # Create Spark session
        spark = (
            SparkSession.builder
            .appName(APP_NAME)
            .getOrCreate()
        )

        # Read Orders CSV using explicit schema
        logger.info("Reading Orders CSV from %s", ORDERS_CSV)
        orders_df = (
            spark.read
            .option("header", True)
            .schema(orders_schema)
            .csv(str(ORDERS_CSV))
        )

        # Validate records
        logger.info("Validating Orders records")
        valid_df, invalid_df, summary = validate_orders(orders_df)

        # Validation summary
        logger.info("Validation Summary: Total Records: %s," \
        " Valid Records: %s," \
        " Invalid Records: %s",
                    summary["total_records"],
                    summary["valid_records"],
                    summary["invalid_records"]
                    )

        # Display schema
        logger.info("Displaying schema for valid records")
        valid_df.printSchema()

        # Display sample valid records
        logger.info("Displaying sample valid records")
        valid_df.show(5, truncate=False)

        # Display invalid records (if any)
        if summary["invalid_records"] > 0:
            logger.info("Displaying sample invalid records")
            invalid_df.show(5, truncate=False)

        # Write Bronze Parquet
        write_parquet(valid_df, BRONZE_ORDERS_DIR)

        # Verify output
        bronze_df = spark.read.parquet(str(BRONZE_ORDERS_DIR))

        logger.info("Bronze Layer Verification")
        logger.info("-------------------------")
        logger.info("Rows Written : %s", bronze_df.count())

        bronze_df.show(5, truncate=False)
        logger.info("Bronze pipeline for Orders completed successfully.")


    except Exception as e:
        logger.exception("Bronze pipeline failed")

    finally:
        if spark is not None:
            spark.stop()


if __name__ == "__main__":
    main()