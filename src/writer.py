def write_parquet(df, output_path):
    """
    Write the DataFrame to the layer in Parquet format.

    Args:
        df (DataFrame): The DataFrame to write.
        output_path (str): The output path for the layer.
    """
    df.write.mode("overwrite").parquet(str(output_path))
