from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.account_schema import AccountCreate, AccountResponse
from app.services import account_service
from app.core.security import get_current_user
from app.models.user_model import User

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/", response_model=List[AccountResponse])
def list_accounts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return account_service.get_all_accounts(db, current_user.id)

@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    account = account_service.get_account_by_id(db, account_id, current_user.id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account

@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return account_service.create_account(db, account, current_user.id)

@router.put("/{account_id}", response_model=AccountResponse)
def update_account(account_id: int, account: AccountCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_account = account_service.get_account_by_id(db, account_id, current_user.id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account_service.update_account(db, db_account, account)

@router.delete("/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    account = account_service.get_account_by_id(db, account_id, current_user.id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    account_service.delete_account(db, account)
    return {"message": "Conta deletada com sucesso"}
