from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime

class TransactionCreate(BaseModel):
    type: Literal["income", "expense"]
    amount: float = Field(..., gt=0)
    description: Optional[str] = None
    date: datetime
    category_id: int
    account_id: int

class TransactionResponse(BaseModel):
    id: int
    type: str
    amount: float
    description: Optional[str]
    date: datetime
    is_active: bool
    user_id: int
    category_id: int
    account_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True