# 09-connect-app-to-db

## 🎯 Problem
Let's connect the app to a real Postgres DB.

## ✅ Your Task
- Add `.env` with env variables app needs (see sample.env)
- In `/api/test-db`, connect to the database and return the current time
- Use `os.getenv` to read config
- Use `psycopg2` to run DB query

## 🧪 Test
- install new libraries: `pip install -r requirements.txt`
- Run the app: `uvicorn main:app --reload`
- Open: http://localhost:8000/api/test-db
- You should see the DB timestamp!

## 📦 Starter Code
- `requirements.txt` - updated
- `sample.env`
- `docker-compose.yml`
- `main.py` — FastAPI app scaffold
