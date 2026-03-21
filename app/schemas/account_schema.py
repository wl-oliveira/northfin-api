from pydantic import BaseModel, Field
from datetime import datetime

# Schemas for Account
# AccountCreate: Schema para criação de conta
class AccountCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    initial_balance: float = Field (default=0.0, ge=0)
# AccountResponse: Schema para resposta de conta
class AccountResponse(BaseModel):
    id: int
    name: str
    initial_balance: float
    current_balance: float
    is_active: bool
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True