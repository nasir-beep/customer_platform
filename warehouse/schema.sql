DROP TABLE IF EXISTS fact_support;
DROP TABLE IF EXISTS fact_orders;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_customer;

CREATE TABLE dim_customer (

    customer_key SERIAL PRIMARY KEY,

    customer_id VARCHAR(50) UNIQUE NOT NULL,

    first_name VARCHAR(100),

    last_name VARCHAR(100),

    email VARCHAR(255),

    gender VARCHAR(20),

    city VARCHAR(100),

    state VARCHAR(100),

    country VARCHAR(100),

    signup_date DATE,

    source VARCHAR(100)

);

CREATE TABLE dim_product (

    product_key SERIAL PRIMARY KEY,

    product_id VARCHAR(50) UNIQUE NOT NULL,

    product_name VARCHAR(255),

    category VARCHAR(100),

    price DECIMAL(10,2)

);

CREATE TABLE dim_date (

    date_key SERIAL PRIMARY KEY,

    full_date DATE UNIQUE,

    day INTEGER,

    month INTEGER,

    month_name VARCHAR(20),

    quarter INTEGER,

    year INTEGER,

    week INTEGER,

    day_of_week VARCHAR(20)

);

CREATE TABLE fact_orders (

    order_key SERIAL PRIMARY KEY,

    order_id VARCHAR(50) UNIQUE,

    customer_key INTEGER,

    product_key INTEGER,

    date_key INTEGER,

    quantity INTEGER,

    order_amount DECIMAL(12,2),

    payment_method VARCHAR(50),

    status VARCHAR(50),

    CONSTRAINT fk_customer

        FOREIGN KEY(customer_key)

        REFERENCES dim_customer(customer_key),

    CONSTRAINT fk_product

        FOREIGN KEY(product_key)

        REFERENCES dim_product(product_key),

    CONSTRAINT fk_date

        FOREIGN KEY(date_key)

        REFERENCES dim_date(date_key)

);

CREATE TABLE fact_support (

    ticket_key SERIAL PRIMARY KEY,

    ticket_id VARCHAR(50) UNIQUE,

    customer_key INTEGER,

    date_key INTEGER,

    issue_type VARCHAR(100),

    resolution_time_hours DECIMAL(8,2),

    sentiment VARCHAR(50),

    support_agent VARCHAR(100),

    CONSTRAINT fk_support_customer

        FOREIGN KEY(customer_key)

        REFERENCES dim_customer(customer_key),

    CONSTRAINT fk_support_date

        FOREIGN KEY(date_key)

        REFERENCES dim_date(date_key)

);