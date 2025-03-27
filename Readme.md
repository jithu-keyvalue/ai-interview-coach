💭 How to evolve DB structure without writing raw SQL like `ALTER TABLE ...`?

🎯 Problem  
Let’s move from create_all to migrations with Alembic.

✅ Your Task  
- Add `alembic` as a dependency in requirements.txt
- Install alembic `pip install ...` 
- Fix models.py as per our target DB table column structure
- Create migration script: `alembic revision --autogenerate -m "Update user table: drop role/place, add email"` (this creates a plan for DB changes)
- Run the migration script: `alembic upgrade head` (this executes the plan)

🧪 Test  
- Run app: `uvicorn main:app --reload` and test user creation and fetch
- Confirm new fields are reflected in DB
