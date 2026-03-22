from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.transaction_schema import TransactionCreate, TransactionResponse
from app.services import transaction_service
from app.core.security import get_current_active_user
from app.models.user_model import User

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/", response_model=List[TransactionResponse])
def list_transactions(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return transaction_service.get_all_transactions(db, current_user.id)


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    transaction = transaction_service.get_transaction_by_id(db, transaction_id, current_user.id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transaction


@router.post("/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return transaction_service.create_transaction(db, transaction, current_user.id)


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    transaction = transaction_service.get_transaction_by_id(db, transaction_id, current_user.id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    transaction_service.delete_transaction(db, transaction)
    return {"message": "Transação deletada com sucesso"}
