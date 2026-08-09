from src.transformations import transform_orders

def test_transform_orders(spark):
    data = [
        ("1", "customer1", "delivered"),
        ("2", "customer2", "shipped")
    ]

    df = spark.createDataFrame(
        data,
        ["order_id", "customer_id", "order_status"]
    )

    transformed_df = transform_orders(df)

    assert "silver_processed_timestamp" in transformed_df.columns

    assert (
        transformed_df
        .filter("silver_processed_timestamp IS NULL")
        .count()
        == 0
    )