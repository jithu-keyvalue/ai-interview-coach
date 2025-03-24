from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    return conn

@app.on_event("startup")
def initialize():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(open("schema.sql").read())  # Load schema
    conn.commit()
    cur.close()
    conn.close()

@app.post("/api/users")
def create_user(data: dict):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, role) VALUES (%s, %s) RETURNING id",  # 📝 TODO: Include place too
        (data["name"], data["role"])
    )
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": user_id, "message": "User profile saved!"}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    # 📝 Todo: get connection first
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM ai_coach_app_users WHERE id = %s", (user_id,))  # 🐛 Fix bug
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
