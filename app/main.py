import os
import logging
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.models import User, Message
from app.database import get_db
from app.schemas import UserCreate, UserOut, LoginInput, UpdateUser, ChatInput
from app.auth import hash_password, verify_password, create_token, get_current_user
from openai import OpenAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@app.post("/api/users", response_model=UserOut, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        logger.warning(f"Signup failed: Email already exists - {user.email}")
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, password_hash=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(f"New user created: {new_user.email} (id={new_user.id})")
    return new_user

@app.post("/api/login")
def login(data: LoginInput, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({ "user_id": user.id })
    return { "token": token }

@app.get("/api/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    return current_user


@app.put("/api/me", response_model=UserOut)
def update_me(data: UpdateUser, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if data.name:
        user.name = data.name
    if data.email:
        user.email = data.email
    if data.password:
        user.password_hash = hash_password(data.password)

    db.commit()
    db.refresh(user)
    return user


@app.delete("/api/me", status_code=204)
def delete_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db.delete(current_user)
    db.commit()
    return


# 📝 TODO: This endpoint is to create a chat message (accept from Front-end, send it to OpenAI, save exchange in our DB)
@app.delete("/api/chat")
def chat(
    data: dict, # 📝 TODO: Is there a more suitable Input schema for this data? check schemas.py
    db: Session = Depends(get_db),
    # 📝 TODO: Inject current user into this method
):
    # 📝 TODO: Currently the history we send to OpenAI will have 50 messages. Let's reduce that. 20 is fine for now.
    past_messages = db.query(Message).filter(Message.user_id == user.id).order_by(Message.id.asc()).limit(50).all()
    history = [
        {"role": m.role, "content": m.content}
        for m in past_messages
    ]

    # Add latest user message to the history
    # 📝 TODO: What should be the role value here?
    # Hint: https://github.com/jithu-keyvalue/ai-interview-coach/blob/notes/Readme.md#18-ai-chat-openai
    history.append({"role": "main", "content": data.message})


    # 📝 TODO: Pass the history to the OpenAI API    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=''
        )
        answer = response.choices[0].message.content
    except Exception as e:
        print("OpenAI error:", e)
        raise HTTPException(status_code=500, detail="AI call failed")

  
    answer = response.choices[0].message.content

    # Save both user question and assistant reply
    # 📝 TODO: something wrong with how we save the assistant's answer?
    db.add(Message(user_id=user.id, role="user", content=data.message))
    db.add(Message(user_id=user.id, role="assistant", content='answer'))
    db.commit()

    return { "reply": answer }

# 📝 TODO: Are we setting the correct HTTP method here?
@app.post("/api/chat/history")
def get_chat_history(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    messages = db.query(Message).filter(Message.user_id == user.id).order_by(Message.id).all()
    return [
        {"role": m.role, "content": m.content}
        for m in messages
    ]
