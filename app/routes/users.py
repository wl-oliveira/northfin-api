from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service
from app.core.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def get_me(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = user_service.get_user_by_email(db, current_user)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.put("/me", response_model=UserResponse)
def update_user(user: UserCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_user = user_service.get_user_by_email(db, current_user)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user_service.update_user(db, db_user, user)


@router.delete("/me")
def delete_user(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = user_service.get_user_by_email(db, current_user)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    user_service.delete_user(db, user)
    return {"message": "Usuário deletado com sucesso"}
