from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

'''

# Define a Pydantic model for data structure and validation
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

# A simple in-memory list to store items (resets on server restart)
items_db = []
'''


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