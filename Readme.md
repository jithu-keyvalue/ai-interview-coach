💭 How can users sign up through a real web page?  

Let’s integrate our backend with a simple frontend and see what issues come up when the browser talks to the API directly.

🎯 Problem  
Create a basic signup form and connect it to the FastAPI backend.  

✅ Your Task  
- Finish signup.html form that uses the POST API for creating users.
- Open file directly in a browser, try signing up and see what happens
- Start serving the HTML using Python’s http.server

- Handle response (success/fail)
- Fix the CORS issue that arises

🧪 Test

Run FastAPI server: `uvicorn main:app --reload`

Serve frontend: `python3 -m http.server 8001`

Open browser:http://localhost:8001/signup.html

Try submitting user details → confirm user created via Swagger /docs