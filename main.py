from fastapi import FastAPI

app = FastAPI()

users = {}

@app.post("/api/users")
def create_user(data):  # 📝 TODO: Add type annotation to read request body
    # 📝 TODO: Save the user data with auto-generated id
    return {"message": "User profile saved!"}

@app.get("/api/users/{id}")
def get_user(id): # 📝 TODO: Add type annotation to read request body
    # 📝 TODO: Return user with given id
    return {}