from sqlalchemy.orm import Session
from pymongo import MongoClient
from python_files.postgres_db_model import Deployment

MONGO_URL = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_URL)

def create_deployment_service(db: Session, db_name: str, username: str) -> int:
    mongo_db = mongo_client[db_name]
    mongo_db["init_collection"].insert_one({"created_by": username})

    deployment = Deployment(db_name=db_name, username=username)
    db.add(deployment)
    db.commit()
    db.refresh(deployment)

    return deployment.id