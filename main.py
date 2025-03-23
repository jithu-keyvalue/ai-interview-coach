from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI()
users = {}

class User(BaseModel):
    name: str = Field(..., min_length=2) # 📝 TODO: enforce max length = 10
    role: Literal["developer", "designer", "product-manager"] # 📝 TODO: allow role "tester" also
    place: str  # 📝 TODO: enforce min length = 2

@app.post("/api/users", status_code=201)
def create_user(user: dict): # 📝 TODO: use correct type
    # if "name" not in user or not isinstance(user["name"], str):
    #     return JSONResponse(status_code=400, content={"error": "Name is required and must be a string"})

    # if "role" not in user or user["role"] not in ALLOWED_ROLES:
    #     return JSONResponse(status_code=400, content={"error": "Unsupported role"})

    # if "place" not in user or not isinstance(user["place"], str):
    #     return JSONResponse(status_code=400, content={"error": "Place is required and must be a string"})
    user_id = len(users) + 1
    users[user_id] = user.model_dump()
    return {"id": user_id, "message": "User profile saved!"}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id, {"error": "User not found"})
