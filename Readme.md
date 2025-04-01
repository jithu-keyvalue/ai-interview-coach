💭 How can the coach respond token-by-token like ChatGPT?  
Let’s use SSE to stream the AI reply as it’s being generated.  

🎯 Problem  
Update the app to support streaming AI responses using Server-Sent Events (SSE).  
The UI should show the reply as it arrives, token by token.  

✅ Your Task  
 - Fix issues in main.py
 - Fix issues in home.html to:

🧪 Test  
 - Start backend: uvicorn app.main:app --reload
 - Start frontend: python -m http.server 8001
 - Open: http://localhost:8001/app/templates/home.html
 - Try chatting with the coach — you should see tokens stream in one by one, like ChatGPT.