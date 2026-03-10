from fastapi import APIRouter
from app.schemas.user_schema import User

router = APIRouter()

users_db = []

@router.get("/users")
def list_users():
    return users_db

@router.post("/users")
def create_user(user: User):
    users_db.append(user)
    return {"message": "Usuário criado com sucesso", "user": user}