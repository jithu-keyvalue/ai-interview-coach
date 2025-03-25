💭 How can the coach remember user data across restarts?
Let’s save it in Postgres using SQL.

🎯 Problem
Persist user data in a real Postgres DB — no more in-memory store!

✅ Your Task
- Complete the schema: Add `role` and `place` fields
- Add missing columns in the `INSERT` query in `create_user`
- Fix/finish `get_user`

🧪 Test
- Run the app: `uvicorn main:app --reload`
- Go to: [http://localhost:8000/docs](http://localhost:8000/docs)
- Test creating users
- Test fetching users

