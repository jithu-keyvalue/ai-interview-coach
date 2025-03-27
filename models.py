from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False) # 📝 TODO: remove role column
    place = Column(String, nullable=False) # 📝 TODO: remove place column
    email = Column(String) 
    password_hash = Column(String, nullable=False)
