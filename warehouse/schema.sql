CREATE SCHEMA IF NOT EXISTS warehouse;

DROP TABLE IF EXISTS warehouse.fact_orders;
DROP TABLE IF EXISTS warehouse.dim_customer;
DROP TABLE IF EXISTS warehouse.dim_product;

CREATE TABLE warehouse.dim_customer (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    city TEXT,
    state TEXT
);

CREATE TABLE warehouse.dim_product (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price NUMERIC
);

CREATE TABLE warehouse.fact_orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    product_id TEXT,
    order_date DATE,
    quantity INT,
    sales NUMERIC
);