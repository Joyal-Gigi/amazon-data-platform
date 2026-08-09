from src.cleansing import (
    cleanse_orders,
    remove_duplicates,
    trim_whitespace,
    normalize_string_case,
)


def test_remove_duplicates(spark):
    data = [
        ("1", "customer1", "delivered"),
        ("1", "customer1", "delivered"),
        ("2", "customer2", "shipped"),
    ]

    df = spark.createDataFrame(
        data,
        ["order_id", "customer_id", "order_status"]
    )

    cleaned_df, duplicate_count = remove_duplicates(df)

    assert duplicate_count == 1
    assert cleaned_df.count() == 2


def test_trim_whitespace(spark):
    data = [
        ("1", " customer1 ", " DELIVERED ")
    ]

    df = spark.createDataFrame(
        data,
        ["order_id", "customer_id", "order_status"]
    )

    cleaned_df = trim_whitespace(df)

    row = cleaned_df.first()

    assert row["customer_id"] == "customer1"
    assert row["order_status"] == "DELIVERED"


def test_normalize_string_case(spark):
    data = [
        ("1", "customer1", " DELIVERED ")
    ]

    df = spark.createDataFrame(
        data,
        ["order_id", "customer_id", "order_status"]
    )

    cleaned_df = normalize_string_case(df)

    row = cleaned_df.first()

    assert row["order_status"] == " delivered "


def test_cleanse_orders(spark):
    data = [
        ("1", " customer1 ", " DELIVERED "),
        ("1", " customer1 ", " DELIVERED "),
        ("2", " customer2 ", " SHIPPED "),
    ]

    df = spark.createDataFrame(
        data,
        ["order_id", "customer_id", "order_status"]
    )

    cleaned_df, duplicate_count = cleanse_orders(df)

    assert duplicate_count == 1
    assert cleaned_df.count() == 2

    rows = cleaned_df.collect()

    assert all(row["customer_id"].strip() == row["customer_id"]
               for row in rows)
    assert all(row["order_status"].lower() == row["order_status"]
               for row in rows)