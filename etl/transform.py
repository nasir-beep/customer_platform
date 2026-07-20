import pandas as pd


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the customer dataset."""

    # Remove duplicate customers
    df = df.drop_duplicates(subset=["customer_id"])

    # Remove leading/trailing spaces from text columns
    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].astype(str).str.strip()

    # Convert signup date
    df["signup_date"] = pd.to_datetime(
        df["signup_date"],
        errors="coerce"
    )

    return df

def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    """Clean product data."""

    df = df.drop_duplicates(subset=["product_id"])

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].astype(str).str.strip()

    # Convert price to numeric
    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    # Remove products with missing or negative prices
    df = df[df["price"].notna()]
    df = df[df["price"] >= 0]

    return df


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Clean order data."""

    df = df.drop_duplicates(subset=["order_id"])

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    df["order_amount"] = pd.to_numeric(
        df["order_amount"],
        errors="coerce"
    )

    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    df = df[df["order_amount"].notna()]
    df = df[df["quantity"] > 0]

    return df


def clean_support(df: pd.DataFrame) -> pd.DataFrame:
    """Clean support ticket data."""

    df = df.drop_duplicates(subset=["ticket_id"])

    df["ticket_created"] = pd.to_datetime(
        df["ticket_created"],
        errors="coerce"
    )

    df["ticket_resolved"] = pd.to_datetime(
        df["ticket_resolved"],
        errors="coerce"
    )

    df["resolution_time_hours"] = pd.to_numeric(
        df["resolution_time_hours"],
        errors="coerce"
    )

    return df