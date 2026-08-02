def write_bronze(df, output_path):
    """
    Write the DataFrame to the Bronze layer in Parquet format.

    Args:
        df (DataFrame): The DataFrame to write.
        output_path (str): The output path for the Bronze layer.
    """
    df.write.mode("overwrite").parquet(str(output_path))
