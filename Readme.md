💭 How can we log in and greet the user securely?  


🎯 Problem  
Implement login functionality using JWT. 
Let the user sign in via UI, store token, and call a protected /api/me to greet them.


✅ Your Task  
- install python-jose dependency
- Fix issues in login.html
- Fix issues in signup.html 
- Fix issues in home.html 
- Complete the LoginInput model in schemas.py
- set JWT_SECRET in env, choose a password-like string
- fix the create_token, decode_token methods in auth.py
- fix the /login, /me APIs in main.py

🧪 Test  
- Serve UI with: python3 -m http.server 8001
- Run FastAPI: uvicorn main:app --reload
- Sign up → Log in → See greeting from /api/me