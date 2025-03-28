💭 How can the coach start chatting like ChatGPT?  
Let’s connect the backend to OpenAI and build a simple UI for chatting.  

🎯 Problem  
Build a chat feature where the coach replies using OpenAI.  
Each message works standalone (no memory yet).  


✅ Your Task  
- Add/install `openai` python library
- Set OPEN AI API Key in an env variable
- Correct issues in main.py:
  - Use the right env variable for OpenAI usage
  - Fix issues in /api/chat API
- Correct issues in home.html:
  - Fix API call issues

🧪 Test  
- Start backend server: `uvicorn app.main:app --reload`
- Start frontned server: `python -m http.server 8001`
- Open Chat: http://localhost:8001/app/templates/home.html
- Test chat