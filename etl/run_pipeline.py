from pathlib import Path

from extract import load_customers
from transform import clean_customers

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

customers = load_customers()
customers = clean_customers(customers)

customers.to_csv(
    OUTPUT_DIR / "customers_clean.csv",
    index=False
)

print("Customer ETL completed successfully.")