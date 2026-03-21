from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database.base import Base
from datetime import datetime

# Modelo para as transações do usuário

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index = True)
    type = Column(String, nullable=False) #income or expense
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    category = relationship("Category")
    account = relationship("Account")
    owner = relationship("User", back_populates="transactions")
