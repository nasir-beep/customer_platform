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