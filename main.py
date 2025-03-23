from fastapi import FastAPI

app = FastAPI()

users = {}

@app.post("/api/users")
def create_user(data: dict):
    user_id = len(users) + 1
    users[user_id] = data
    return {"id": user_id, "message": "User profile saved!"}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id, {"error": "User not found"})

@app.get("/api/users/{user_id}") # 📝 TODO: Correct HTTP method
def update_user(user_id: int, data):  # 📝 TODO: Add type annotation for body
    # 📝 TODO: Update user data if user exists
    pass

@app.get("/api/users/{user_id}") # 📝 TODO: Correct HTTP method
def delete_user(user_id: int):
    # 📝 TODO: Delete user if user exists
    pass
