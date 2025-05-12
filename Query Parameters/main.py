import uvicorn 
from fastapi import FastAPI


print("\n\t Server is Running..... \t\n")
app = FastAPI()

@app.get("/users/{user_name}")
async def read_user(user_name: str | None = None):
    """
    this is a simple FastAPI application that returns the user_data passed in the URL. 
    The user_data can be an integer, string, and if None is passed, it will return None.
    """
    if user_name.isdigit():
        return {'user_id': int(user_name)}
    return {'user_id': user_name}