from jose import jwt
from datetime import datetime, timedelta, timezone
import os

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
EXPIRY_MINUTES = 60

# 📝 TODO: use EXPIRY_MINUTES to set how long the token should be valid
def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=60000)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

 # 📝 TODO: use the correct secret to decode
def decode_token(token: str):
    return jwt.decode(token, "some_secret", algorithms=[ALGORITHM]) 
