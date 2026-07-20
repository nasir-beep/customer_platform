import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from etl.extract import (
    load_customers,
    load_products,
    load_orders,
    load_support,
)

print("Customers:", load_customers().shape)
print("Products:", load_products().shape)
print("Orders:", load_orders().shape)
print("Support:", load_support().shape)