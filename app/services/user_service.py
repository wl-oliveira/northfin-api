from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age,
        phone=user.phone
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def update_user(db: Session, db_user: User, user: UserCreate):
    db_user.name = user.name
    db_user.email = user.email
    db_user.age = user.age
    db_user.phone = user.phone

    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db: Session, user):
    db.delete(user)
    db.commit()