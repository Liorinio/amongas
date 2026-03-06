from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from python_files.schamas_and_models.schemas import DeploymentCreate
from functionallity.create_db import create_deployment_service
from getting_db import get_db
from functionallity.get_details_via_id import get_deployment_service

app = FastAPI()

@app.post("/deployments")
def create_db(payload: DeploymentCreate, db: Session = Depends(get_db)):
        try:
            deployment_id = create_deployment_service(db=db,db_name=payload.db_name,username=payload.username)
        except ValueError as e:
            raise HTTPException(status_code=400,detail=str(e))

        return {"id": str(deployment_id)}

@app.get("/deployments/:<deployment_id>")
def get_deployment_properties(deployment_id):
    get_deployment_service(deployment_id)

@app.put("/deployments/:deployment_id")
def update_deployment_name():
    ...

@app.delete("/deployments/:<deployment_id>")
def delete_db():
    ...

@app.get("/deployments/connection_string/:<deployment_id>")
def get_connection_string():
    ...