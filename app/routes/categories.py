from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.category_schema import CategoryCreate, CategoryResponse
from app.services import category_service
from app.core.security import get_current_active_user
from app.models.user_model import User

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[CategoryResponse])
def list_categories(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return category_service.get_all_categories(db, current_user.id)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    category = category_service.get_category_by_id(db, category_id, current_user.id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return category

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return category_service.create_category(db, category, current_user.id)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_category = category_service.get_category_by_id(db, category_id, current_user.id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return category_service.update_category(db, db_category, category)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    category = category_service.get_category_by_id(db, category_id, current_user.id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    category_service.delete_category(db, category)
    return {"message": "Categoria deletada com sucesso"}