from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer)
    phone = Column(String)
    is_active = Column(Boolean, default=True)

    accounts = relationship("Account", back_populates="owner")
    categories = relationship("Category", back_populates="owner")
    transactions = relationship("Transaction", back_populates="owner")