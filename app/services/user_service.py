from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    print(user.password)
    print(len(user.password))
    print(len(user.password.encode('utf-8')))


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
    
    return new_user

def update_user(db: Session, db_user: User, user: UserCreate):
    db_user.name = user.name
    db_user.email = user.email
    db_user.password=get_password_hash(user.password)
    db_user.age = user.age
    db_user.phone = user.phone
    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db: Session, user):
    db.delete(user)
    db.commit()