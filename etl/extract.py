from pathlib import Path
import pandas as pd

RAW_DATA = Path("data/raw")


def load_customers():
    return pd.read_csv(RAW_DATA / "crm_50000_customers_dirty_v3.csv")


def load_products():
    return pd.read_csv(RAW_DATA / "product_catalog_dirty_30pct.csv")


def load_orders():
    return pd.read_csv(RAW_DATA / "orders_300k_dirty.csv")


def load_support():
    return pd.read_csv(RAW_DATA / "support_tickets_30000_dirty.csv")