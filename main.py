from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/deployments/:<deployment_id>")
def get_deployment_properties():
    ...

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