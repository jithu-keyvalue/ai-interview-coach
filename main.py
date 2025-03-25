from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def hello_world():
    return "Hello world!"

# 📝 TODO:  Add the GET /api/time endpoint here
