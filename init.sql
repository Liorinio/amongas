CREATE SCHEMA IF NOT EXISTS oltp;

CREATE TABLE IF NOT EXISTS oltp.user_transactions
(
    id INT
    db_name VARCHAR
    status VARCHAR
    username VARCHAR
    creation_time TIMESTAMP
)


