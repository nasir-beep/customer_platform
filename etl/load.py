from pathlib import Path

import pandas as pd

from database import engine
from date_dimension import build_date_dimension

PROCESSED = Path("data/processed")

def load_customers():

    print("Loading customers...")

    customers = pd.read_csv(
        PROCESSED / "customers_clean.csv"
    )

    columns = [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "gender",
        "city",
        "state",
        "country",
        "signup_date",
        "source",
    ]

    customers[columns].to_sql(
        "dim_customer",
        engine,
        if_exists="append",
        index=False,
        method="multi",
    )

    print(f"{len(customers)} customers loaded.")

def load_products():

    print("Loading products...")

    products = pd.read_csv(
        PROCESSED / "products_clean.csv"
    )

    columns = [
        "product_id",
        "product_name",
        "category",
        "price",
    ]

    products[columns].to_sql(
        "dim_product",
        engine,
        if_exists="append",
        index=False,
        method="multi",
    )

    print(f"{len(products)} products loaded.")

def load_dates():

    print("Loading dates...")

    dates = build_date_dimension()

    dates.to_sql(
        "dim_date",
        engine,
        if_exists="append",
        index=False,
        method="multi",
    )

    print(f"{len(dates)} dates loaded.")