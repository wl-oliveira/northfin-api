from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime

class DebtCreate(BaseModel):
    status:  Literal["open", "paid"]
    name: str
    total_amount: float = Field(..., gt=0)
    interest_rate: float = Field(..., ge=0)
    is_installment: bool
    total_installments: Optional[int] = None
    due_date: datetime
    account_id: int

class DebtResponse(BaseModel):
    id: int
    name: str
    total_amount: float
    status: str
    interest_rate: float
    is_installment: bool
    total_installments: Optional[int]
    due_date: datetime 
    remaining_installments: Optional[int]
    paid_at: Optional[datetime] = None
    is_active: bool
    account_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True