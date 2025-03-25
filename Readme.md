💭 What’s the right way to handle user credentials securely?  

We need to store passwords securely (not in plain text), and avoid exposing them in API responses.  

🎯 Problem  
Securely store user credentials using password hashing and proper response handling.  

✅ Your Task  
- Add a hashed version of password using passlib
- Do NOT store or return plain passwords
- Use Pydantic models:
  - `UserCreate` for request
  - `UserOut` for response (exclude password)
- Use `response_model` in endpoints

🧪 Test  
- Install deps: `pip install -r requirements.txt`
- Run the app: `uvicorn main:app --reload`
- Try POST /api/users and GET /api/users/{id} via Swagger (/docs)
- Ensure password is not returned in response

📎 Note: 
If you're re-running after modifying schema.sql, make sure to:
- Uncomment `ALTER TABLE` statement for first run
- Comment it out after running once (to avoid errors)
