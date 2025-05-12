# import uvicorn
# from fastapi import FastAPI

# app = FastAPI()


# class data_type:
#     pass


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

import uvicorn 
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name: str
    age: int | None = None
    ''' this is optional if the data is not available then it will show "none" on the API'''
    Roll_No: int
    message: str


user = User(name="Mujtaba", Roll_No=43160, message="FASTAPI with Pydantic",)



@app.get("/")
def read_root():
    return user.dict()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}