from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lower, trim
from pyspark.sql.types import StringType

def cleanse_orders(df: DataFrame) -> DataFrame:
    """
    Apply business transformations to Orders data.

    Returns:
        Transformed Orders DataFrame.
    """
    df = df.dropDuplicates(["order_id"]) #Drop duplicates based on order_id
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name))) #Trim whitespace from all string columns
    df = df.withColumn("order_status", lower(col("order_status"))) #Convert order_status to lowercase

    return df