from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service
from app.core.security import get_current_user
from app.models.user_model import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.put("/me", response_model=UserResponse)
def update_user(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user_service.update_user(db, current_user, user)


@router.delete("/me")
def delete_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service.delete_user(db, current_user)
    return {"message": "Usuário deletado com sucesso"}
