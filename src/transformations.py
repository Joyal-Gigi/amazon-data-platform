from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp

def transform_orders(df: DataFrame) -> DataFrame:
    """
    Apply business transformations to Orders data.

    Returns:
        Transformed Orders DataFrame.
    """
    df = df.withColumn("silver_processed_timestamp", current_timestamp()) #Add current timestamp

    return df