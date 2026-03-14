from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user_schema import UserCreate
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/ping")
def ping():
    return {"message": "pong"}
@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.put("/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found") 
    
    return user_service.update_user(db, db_user, user)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail= "User not found")
    
    user_service.delete_user(db, user)

    return {"message": "Usuário deletado com sucesso"}
