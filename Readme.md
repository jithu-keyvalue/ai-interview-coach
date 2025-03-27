💭 How can users sign up through a real web page?  

Let’s integrate our backend with a simple frontend.

We will see what issues come up when the browser talks to the API directly.

🎯 Problem  
Create a basic signup form and connect it to the FastAPI backend.  

✅ Your Task  
1. Finish signup.html by correcting the API call.
2. Open signup.html file directly in a browser.
3. Try signing up and see what happens in network tab/console.
4. Bring up a separate server to serve the website using Python’s built-in server: (`python3 -m http.server 8001`)
5. Access webpage via that server http://localhost:8001/signup.html
6. Try signing up and see what happens in network tab/console.
7. Allow requests from origin "http://localhost:8001" in app
8. Try signing up. Confirm user got added via /docs