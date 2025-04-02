💭 Can we make the coach respond in real-time... over WebSockets?  
Let’s upgrade from SSE to WebSockets for better control and interactivity.  

🎯 Problem  
Switch the streaming implementation from SSE to WebSockets.  
The coach’s reply should still appear token by token, but now using a persistent WebSocket connection.   

✅ Your Task  
 - Fix issues in main.py
 - Fix issues in home.html

🧪 Test  
 - Start backend: uvicorn app.main:app --reload
 - Start frontend: python -m http.server 8001
 - Open: http://localhost:8001/app/templates/home.html
 - Chat with the coach — responses should stream token by token, just like before, but now powered by WebSockets.