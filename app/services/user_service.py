from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash

# Serviços para manipulação de usuários
def get_all_users(db: Session):
    return db.query(User).filter(User.is_active == True).all()

# Serviço para obter um usuário por ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id, User.is_active == True).first()

# Serviço para obter um usuário por email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Serviço para criar um novo usuário
def create_user(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email):
        raise HTTPException (status_code=400, detail="Email já cadastrado")


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

# Serviço para atualizar um usuário existente
def update_user(db: Session, db_user: User, user: UserCreate):
    db_user.name = user.name
    db_user.email = user.email
    db_user.password=get_password_hash(user.password)
    db_user.age = user.age
    db_user.phone = user.phone
    db.commit()
    db.refresh(db_user)

    return db_user

# Serviço para deletar um usuário
def delete_user(db: Session, user: User):
    user.is_active = False
    db.commit()