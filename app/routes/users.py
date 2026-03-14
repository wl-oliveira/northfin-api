from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service
from app.core.security import get_current_user
# Rotas para manipulação de usuários
router = APIRouter(prefix="/users", tags=["Users"])

# Rota de teste para verificar se a API está funcionando
@router.get("/ping")
def ping():
    return {"message": "pong"}

# Rota protegida para testar autenticação
@router.get("/me/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": "Rota protegida", "user": current_user}

# Rota para listar todos os usuários
@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return user_service.get_all_users(db)

# Rota para obter um usuário por ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

# Rota para criar um novo usuário
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

# Rota para atualizar um usuário existente
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_user = user_service.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user_service.update_user(db, db_user, user)

# Rota para deletar um usuário
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    user_service.delete_user(db, user)
    return {"message": "Usuário deletado com sucesso"}
