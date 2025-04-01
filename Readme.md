💭 How can we make the chat a real conversation?  
Let’s make the coach remember recent messages — so replies feel more contextual.  


🎯 Problem  
Enable conversation memory by storing chat messages in a DB.  


⚙️ Pre-requisites  
If you remember, we picked up alembic after using raw SQL(`CREATE TABLE ...`) via `schema.sql` to create the table in DB.  
This means, we don't have the alembic migration script that creates the tables.  
This mixed setup is not great:  
- we need to now keep `schema.sql` and run that first in any system that we want to newly deploy in.  
- then we need to run the alembic migrations.  


Better use any one approach - let's go with alembic for convenience - from step 1(user table creation) itself.  
To do that please use these commands to recreate DB:  
- `sudo docker compose down -v`  
- `sudo docker compose up`  
- Run the migration script `alembic upgrade head` (to create the DB tables)
- Start backend: uvicorn app.main:app --reload
- Start frontend: python -m http.server 8001
- Create a user, login


✅ Your Task  
  - Fix issues in main.py
  - Fix issues in home.html 


🧪 Test  
  - Chat: http://localhost:8001/app/templates/home.html
  - Try a multi-turn conversation. Coach should remember!