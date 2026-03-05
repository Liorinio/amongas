from fastapi import FastAPI, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pymongo import MongoClient
from postgres_db_model import Base, Deployment
from schemas import DeploymentCreate
from fastapi import Depends

app = FastAPI()

@app.get("/deployments/:<deployment_id>")
def get_deployment_properties():
    create_deployment_service()

@app.post("/deployments")
def create_db():
    ...

@app.put("/deployments/:deployment_id")
def update_deployment_name():
    ...

@app.delete("/deployments/:<deployment_id>")
def delete_db():
    ...

@app.get("/deployments/connection_string/:<deployment_id>")
def get_connection_string():
    ...