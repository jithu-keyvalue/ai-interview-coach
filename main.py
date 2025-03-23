from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
users = {}

ALLOWED_ROLES = {"developer", "designer", "product-manager"}

@app.post("/api/users")
def create_user(data: dict):
    # ✅ Validate name exists and is a string
    if "name" not in data or not isinstance(data["name"], str):
        return JSONResponse(status_code=400, content={"error": "Invalid or missing name"})

    # 📝 TODO: Validate role is in ALLOWED_ROLES
    # 📝 TODO: Validate place exists and is a string

    user_id = len(users) + 1
    users[user_id] = data
    return {"id": user_id, "message": "User profile saved!"}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    # 📝 TODO: Return 404 if user_id is not found 
    return users[user_id]
