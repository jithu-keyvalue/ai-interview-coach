💭 How to stop writing raw SQL and work with Python objects instead?  

Let’s use SQLAlchemy ORM to define our DB structure and interact with it like real Python code.  

🎯 Problem  
Use SQLAlchemy to define the User table and rewrite the POST and GET endpoints using the ORM — no raw SQL.

⚠️ Manual Step (Do This First)  
  `docker exec -it interview-db psql -U <user> -d <db>`
  `DROP TABLE users;`  

This ensures SQLAlchemy can create it cleanly on startup.  

✅ Your Task  
- Add `sqlalchemy` to requirements.txt
- Create a SQLAlchemy User model (id, name, role, place, password_hash)
- On startup, create the table with Base.metadata.create_all()
- Update /api/users and /api/users/{id} to use SQLAlchemy instead of psycopg2


🧪 Test  
- `pip install -r requirements.txt`  (for SQLAlchemy)
- `uvicorn main:app --reload`
- POST & GET user via Swagger UI - should work as before, now powered by SQLAlchemy