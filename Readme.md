💭 What’s the right way to handle user credentials securely?  

We need to store passwords securely (not in plain text), and avoid exposing them in API responses.  

🎯 Problem  
Securely store user credentials using password hashing and proper response handling.  

✅ Your Task  
- Use schema.sql to update the column name to password_hash

- Do NOT store plain password: store hashed password instead

- Use Pydantic models:
  - `UserCreate` for validating input
  - `UserOut` for response (to exclude password)
- Use `response_model` in endpoints

🧪 Test  
- Install new dependency passlib[bcrypt]: `pip install -r requirements.txt`
- Run the app: `uvicorn main:app --reload`
- Try POST /api/users and GET /api/users/{id} via Swagger (/docs)
- Ensure password is not returned in response

📎 Note: 
- Uncomment `ALTER TABLE` statement for first app run
- Comment it out after running once (to avoid errors)
