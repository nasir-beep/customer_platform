CREATE TABLE IF NOT EXISTS warehouse.fact_support (

    ticket_key SERIAL PRIMARY KEY,

    ticket_id VARCHAR(50) UNIQUE,

    customer_id VARCHAR(50),

    ticket_created DATE,

    ticket_resolved DATE,

    resolution_time_hours NUMERIC(10,2),

    issue_type VARCHAR(100),

    sentiment VARCHAR(50),

    support_agent VARCHAR(100)
);