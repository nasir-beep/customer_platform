CREATE TABLE IF NOT EXISTS warehouse.dim_customer (

    customer_key SERIAL PRIMARY KEY,

    customer_id VARCHAR(50) UNIQUE,

    first_name VARCHAR(100),

    last_name VARCHAR(100),

    gender VARCHAR(20),

    dob DATE,

    city VARCHAR(100),

    state VARCHAR(100),

    country VARCHAR(100),

    signup_date DATE,

    source VARCHAR(100)

);