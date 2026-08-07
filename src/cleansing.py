from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lower, trim
from pyspark.sql.types import StringType


def remove_duplicates(df: DataFrame) -> tuple[DataFrame, int]:
    """
    Remove duplicate Orders using order_id as the business key.

    Returns:
        Tuple containing:
        - Deduplicated DataFrame
        - Number of duplicate records removed
    """

    before_count = df.count()

    deduplicated_df = df.dropDuplicates(["order_id"])

    after_count = deduplicated_df.count()

    duplicate_count = before_count - after_count

    return deduplicated_df, duplicate_count


def trim_whitespace(df: DataFrame) -> DataFrame:
    """Trim whitespace from all string columns."""

    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))

    return df


def normalize_string_case(df: DataFrame) -> DataFrame:
    """Normalize string columns."""

    df = df.withColumn(
        "order_status",
        lower(col("order_status"))
    )

    return df


def cleanse_orders(df: DataFrame) -> tuple[DataFrame, int]:
    """
    Apply data cleansing rules to Orders data.
    """

    df, duplicate_count = remove_duplicates(df)

    df = trim_whitespace(df)

    df = normalize_string_case(df)

    return df, duplicate_count