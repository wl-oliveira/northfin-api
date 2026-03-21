from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.transaction_schema import TransactionCreate, TransactionResponse
from app.services import transaction_service
from app.core.security import get_current_user
from app.services.user_service import get_user_by_email

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/", response_model=List[TransactionResponse])
def list_transactions(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    return transaction_service.get_all_transactions(db, user.id)

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    transaction = transaction_service.get_transaction_by_id(db, transaction_id, user.id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transaction
    
@router.post("/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db), current_user: str =  Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    return transaction_service.create_transaction(db, transaction, user.id)

@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    transaction = transaction_service.get_transaction_by_id(db, transaction_id, user.id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    transaction_service.delete_transaction(db, transaction)
    return {"message": "Transação deletada com sucesso"}