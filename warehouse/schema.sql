DROP TABLE IF EXISTS fact_support;
DROP TABLE IF EXISTS fact_orders;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_date;

CREATE TABLE dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(50) UNIQUE,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    signup_date DATE
);

CREATE TABLE dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(50) UNIQUE,
    product_name VARCHAR(255),
    category VARCHAR(100),
    price NUMERIC(10,2)
);

CREATE TABLE dim_date (
    date_key SERIAL PRIMARY KEY,
    full_date DATE UNIQUE,
    day INTEGER,
    month INTEGER,
    year INTEGER,
    quarter INTEGER
);

CREATE TABLE fact_orders (
    order_key SERIAL PRIMARY KEY,
    order_id VARCHAR(50) UNIQUE,
    customer_key INTEGER REFERENCES dim_customer(customer_key),
    product_key INTEGER REFERENCES dim_product(product_key),
    date_key INTEGER REFERENCES dim_date(date_key),
    quantity INTEGER,
    order_amount NUMERIC(12,2),
    payment_method VARCHAR(50),
    status VARCHAR(50)
);

CREATE TABLE fact_support (
    ticket_key SERIAL PRIMARY KEY,
    ticket_id VARCHAR(50) UNIQUE,
    customer_key INTEGER REFERENCES dim_customer(customer_key),
    date_key INTEGER REFERENCES dim_date(date_key),
    priority VARCHAR(50),
    status VARCHAR(50),
    resolution_time_hours NUMERIC(10,2)
);