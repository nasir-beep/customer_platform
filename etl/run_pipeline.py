from pathlib import Path

from extract import (
    load_customers,
    load_orders,
    load_products,
    load_support,
)

from transform import (
    clean_customers,
    clean_orders,
    clean_products,
    clean_support,
)

OUTPUT = Path("data/processed")
OUTPUT.mkdir(exist_ok=True)

datasets = [
    (
        load_customers(),
        clean_customers,
        "customers_clean.csv",
    ),
    (
        load_products(),
        clean_products,
        "products_clean.csv",
    ),
    (
        load_orders(),
        clean_orders,
        "orders_clean.csv",
    ),
    (
        load_support(),
        clean_support,
        "support_clean.csv",
    ),
]

for dataframe, cleaner, filename in datasets:

    cleaned = cleaner(dataframe)

    cleaned.to_csv(
        OUTPUT / filename,
        index=False
    )

    print(f"Saved {filename}")

print("=" * 50)

for dataframe, cleaner, filename in datasets:

    print(f"Processing {filename}...")

    cleaned = cleaner(dataframe)

    print(f"Rows: {len(cleaned)}")

    cleaned.to_csv(
        OUTPUT / filename,
        index=False
    )

    print(f"Saved {filename}")

    print("-" * 50)

print("ETL completed successfully.")