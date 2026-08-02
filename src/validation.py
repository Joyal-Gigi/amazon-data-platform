from pyspark.sql.functions import col

# Validate the orders DataFrame based on specific conditions
def validate_orders(df):

    """
    Validate the Orders DataFrame.

    Returns:
        tuple:
            valid_df,
            invalid_df,
            validation_summary
    """

    # Define conditions for invalid records
    invalid_condition = (
        (col("order_id").isNull()) |
        (col("order_id") == "") |
        (col("customer_id").isNull()) |
        (col("customer_id") == "") |
        (col("order_status").isNull()) |
        (col("order_status") == "") |
        (col("order_purchase_timestamp").isNull())
    )

    # Filter the DataFrame into valid and invalid records
    valid_df = df.filter(~invalid_condition)
    invalid_df = df.filter(invalid_condition)

    # Create a summary of the validation results
    validation_summary = {
        "total_records": df.count(),
        "valid_records": valid_df.count(),
        "invalid_records": invalid_df.count()
    }

    return valid_df, invalid_df, validation_summary