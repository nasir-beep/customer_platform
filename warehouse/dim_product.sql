CREATE TABLE IF NOT EXISTS warehouse.dim_product (

    product_key SERIAL PRIMARY KEY,

    product_id VARCHAR(50) UNIQUE,

    product_name VARCHAR(255),

    category VARCHAR(100),

    price NUMERIC(10,2)

);