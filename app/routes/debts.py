from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.debt_schema import DebtCreate, DebtResponse
from app.services import debt_service
from app.core.security import get_current_user
from app.services.user_service import get_user_by_email

router = APIRouter(prefix="/debts", tags=["Debts"])

@router.get("/", response_model=List[DebtResponse])
def list_debt(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    return debt_service.get_all_debts(db, user.id)

@router.get("/{debt_id}", response_model=DebtResponse)
def get_debt(debt_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    debt = debt_service.get_debt_by_id(db, debt_id, user.id)
    if not debt: 
        raise HTTPException(status_code=404, detail = "Dívida não encontrado")
    return debt

@router.post("/", response_model=DebtResponse)
def create_debt(debt: DebtCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    return debt_service.create_debt(db, debt, user.id)

@router.put("/{debt_id}", response_model=DebtResponse)
def update_debt(debt_id: int, debt: DebtCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    db_debt = debt_service.get_debt_by_id(db, debt_id, user.id)
    if not db_debt:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    return debt_service.update_debt(db, db_debt, debt)

@router.delete("/{debt_id}")
def delete_debt(debt_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    debt = debt_service.get_debt_by_id(db, debt_id, user.id)
    if not debt: 
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    debt_service.delete_debt(db, debt)
    return {"message": "Dívida deletada com sucesso"}