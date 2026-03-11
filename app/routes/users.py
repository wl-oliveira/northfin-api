from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name = user.name,
        email = user.email,
        age = user.age
    )
   
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user