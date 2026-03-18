from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.base import Base

# Modelo de conta bancária
class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    initial_balance = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    user_id= Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="accounts")