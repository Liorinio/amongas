import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from python_files.schamas_and_models.schemas import DeploymentCreate
from functionallity.create_db import create_deployment_service
from getting_db import get_db
from functionallity.get_details_via_id import get_deployment_service
from functionallity.updating_name import update_name

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
    try:
        details = get_deployment_service(deployment_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"details": details}

@app.put("/deployments/:deployment_id")
def update_deployment_name(deployment_id):
    try:
        update_name(deployment_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    raise HTTPException(status_code=200, detail="The update was successful")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)