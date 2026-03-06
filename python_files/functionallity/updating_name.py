from pydantic import UUID4
from typing import Optional
from python_files.postgres_db_model import Deployment
import psycopg2


def update_name(deployment_id: UUID4) -> Optional[Deployment]:
    query = f"UPDATE db_name, status,creation_time FROM oltp.deployments WHERE id = '{str(deployment_id)};"
    connect_to_postgres(query)


def connect_to_postgres(query):
    connection = psycopg2.connect(database="amongas_db", user="postgres", password="postgres", host="postgres", port=5432)
    cursor = connection.cursor()
    execute_select_query(cursor, query)


def execute_select_query(cursor, query):
    cursor.execute(query =query)
    record = cursor.fetchall()
    return record
