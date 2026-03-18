from pydantic import BaseModel

# Schemas for Account
# AccountCreate: Schema para criação de conta
class AccountCreate(BaseModel):
    name: str
    initial_balance: float = 0.0
# AccountResponse: Schema para resposta de conta
class AccountResponse(BaseModel):
    id: int
    name: str
    initial_balance: float
    is_active: bool
    user_id: int

class Config:
    from_attributes = True