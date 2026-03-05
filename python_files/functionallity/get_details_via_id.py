from pydantic import UUID4
from typing import Optional
from python_files.postgres_db_model import Deployment
import psycopg2

def get_deployment_service(deployment_id: UUID4) -> Optional[Deployment]:
    connect_to_postgres(deployment_id)


def connect_to_postgres(deployment_id):
    connection = psycopg2.connect(database="amongas_db", user="postgres", password="postgres", host="postgres", port=5432)
    cursor = connection.cursor()
    execute_select_query(cursor, deployment_id)


def execute_select_query(cursor, given_id):
    cursor.execute(query = f"SELECT db_name, status,creation_time FROM oltp.deployments WHERE id = '{str(given_id)}';")
    record = cursor.fetchall()
    return record