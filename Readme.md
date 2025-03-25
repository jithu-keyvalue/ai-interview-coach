💭 How can coach talk to the database?
Let’s test a real DB connection from our app!

🎯 Problem
Connect the app to a real Postgres DB.

✅ Your Task
- Add `.env` with env variables app needs (see sample.env)
- In `/api/test-db`, connect to the database and return the current time
- Use `os.getenv` to read config
- Use `psycopg2` to run DB query

🧪 Test
- install new libraries: `pip install -r requirements.txt`
- Run the app: `uvicorn main:app --reload`
- Open: http://localhost:8000/api/test-db
- You should see the DB timestamp!