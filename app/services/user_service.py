from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash
from app.services.category_service import create_default_categories


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id, User.is_active == True).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email, User.is_active == True).first()


def _email_exists(db: Session, email: str) -> bool:
    return db.query(User).filter(User.email == email).first() is not None


def create_user(db: Session, user: UserCreate):
    if _email_exists(db, user.email):
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    new_user = User(
        name=user.name,
        email=user.email,
        password=get_password_hash(user.password),
        age=user.age,
        phone=user.phone
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    create_default_categories(db, new_user.id)

    return new_user


def update_user(db: Session, db_user: User, user: UserCreate):
    if user.email != db_user.email and _email_exists(db, user.email):
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    db_user.name = user.name
    db_user.email = user.email
    db_user.password = get_password_hash(user.password)
    db_user.age = user.age
    db_user.phone = user.phone
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: User):
    user.is_active = False
    db.commit()
