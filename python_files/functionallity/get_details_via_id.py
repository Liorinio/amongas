from pydantic import UUID4
from typing import Optional
from python_files.schamas_and_models.postgres_db_model import Deployment
from python_files.services.posgres_services import connect_to_postgres

def get_deployment_service(deployment_id: UUID4) -> Optional[Deployment]:
    query = f"SELECT db_name, status,creation_time FROM oltp.deployments WHERE id = '{str(deployment_id)};"
    connect_to_postgres(query)


