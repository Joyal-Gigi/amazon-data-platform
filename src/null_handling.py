def handle_nulls(df):
    """
    Apply the null handling strategy for Orders.

    - Mandatory fields are validated in validation.py.
    - Optional timestamp fields are preserved as NULL because
      they represent valid business states (e.g. pending approval
      or delivery).

    Returns:
        DataFrame with the null handling strategy applied.
    """
    return df
