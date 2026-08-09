from src.validation import validate_orders

def test_validate_orders(spark):
    data = [
        ("1", "customer1", "delivered", "2023-01-01 10:00:00"),
        (None, "customer2", "shipped", "2023-01-02 11:00:00"),
        ("3", None, "pending", "2023-01-03 12:00:00"),
        ("4", "customer4", None, "2023-01-04 13:00:00"),
        ("5", "customer5", "cancelled", None),
    ]

    df = spark.createDataFrame(
        data,
        ["order_id", "customer_id", "order_status", "order_purchase_timestamp"]
    )

    valid_df, invalid_df, validation_summary = validate_orders(df)

    assert validation_summary["total_records"] == 5
    assert validation_summary["valid_records"] == 1
    assert validation_summary["invalid_records"] == 4

    assert valid_df.count() == 1
    assert invalid_df.count() == 4