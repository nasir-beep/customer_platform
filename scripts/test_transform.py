import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from etl.extract import load_customers
from etl.transform import clean_customers

customers = load_customers()

print("Before:", customers.shape)

customers = clean_customers(customers)

print("After:", customers.shape)

print(customers.head())