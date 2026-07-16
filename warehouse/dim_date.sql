CREATE TABLE IF NOT EXISTS warehouse.dim_date (

    date_key INTEGER PRIMARY KEY,

    full_date DATE,

    day INTEGER,

    month INTEGER,

    month_name VARCHAR(20),

    quarter INTEGER,

    year INTEGER,

    day_of_week VARCHAR(20)

);