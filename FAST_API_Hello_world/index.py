from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    origin: str
    
data: list[Item] = []

@app.get("/")
def read_root():
    return {"name": "Mujtaba Chandio",
            "Roll No": 43160,
            "message": "Hello World"}
