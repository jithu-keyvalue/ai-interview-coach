💭 How to evolve DB structure without writing raw SQL like `ALTER TABLE ...`?

🎯 Problem  
Let’s move from create_all to migrations with Alembic.

✅ Your Task  
- Fix models.py as per our target DB table column structure
- Add `alembic` as a dependency in requirements.txt
- Install alembic `pip install ...` 
- Initialize alembic: `alembic init alembic`
- Update this line in alembic.ini: `sqlalchemy.url = driver://user:pass@localhost/dbname` to `sqlalchemy.url = postgresql://aic_user:aic_pwd@localhost:5434/aic_db`
- Update alembic/env.py:
  - Replace these lines:
    - `# from myapp import mymodel`
    - `# target_metadata = mymodel.Base.metadata`
    - `target_metadata = None`
  - with
    - `from models import Base`
    - `target_metadata = Base.metadata`
- Create migration script: `alembic revision --autogenerate -m "Update user table: drop role/place, add email"`
- Run the migration script: `alembic upgrade head`

🧪 Test  
- Test user creation and fetch
- Confirm new fields are reflected in DB
