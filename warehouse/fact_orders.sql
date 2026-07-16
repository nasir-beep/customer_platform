CREATE TABLE IF NOT EXISTS warehouse.fact_orders (

    order_key SERIAL PRIMARY KEY,

    order_id VARCHAR(50) UNIQUE,

    customer_id VARCHAR(50),

    product_id VARCHAR(50),

    order_date DATE,

    quantity INTEGER,

    order_amount NUMERIC(12,2),

    payment_method VARCHAR(50),

    status VARCHAR(50)
);