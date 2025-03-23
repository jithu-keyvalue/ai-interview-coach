# 02-hello-api-time

## 🎯 Problem
Make the coach tell the current server time via an API.

## ⚙️ Pre-requisites
- Create virtual environment (only once): `python3 -m venv .venv`
- Activate it: `source .venv/bin/activate`
- Install required libraries: `pip install -r requirements.txt`

## 📦 Already Included
- main.py — FastAPI app skeleton
- requirements.txt 

## ✅ Your Task
- Add /api/time endpoint
- Response format: { "time": <current_timestamp> }
  - Use datetime.datetime.now()

## 🧪 Test
-  Run the Server: `uvicorn main:app --reload`
- Check http://localhost:8000/api/time