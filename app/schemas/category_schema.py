from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    type: Literal["income", "expense"]


class CategoryResponse(BaseModel):
    id: int
    name: str
    type: str
    is_default: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime
    user_id: int

    class Config:
        from_attributes = True
