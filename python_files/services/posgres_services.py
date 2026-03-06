import psycopg2


def connect_to_postgres(query):
    connection = psycopg2.connect(database="amongas_db", user="postgres", password="postgres", host="postgres", port=5432)
    cursor = connection.cursor()
    return execute_select_query(cursor, query)


def execute_select_query(cursor, query):
    cursor.execute(query =query)
    record = cursor.fetchall()
    return record