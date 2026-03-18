from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.account_schema import AccountCreate, AccountResponse
from app.services import account_service
from app.core.security import get_current_user
from app.services.user_service import get_user_by_email

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/", response_model=List[AccountResponse])
def list_accounts(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    return account_service.get_all_accounts(db, user.id)

@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    account = account_service.get_account_by_id(db, account_id, user.id)
    if not account: 
        raise HTTPException(status_code=404, detail = "Conta não encontrada")
    return account

@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    return account_service.create_account(db, account, user.id)

@router.put("/{account_id}", response_model=AccountResponse)
def update_account(account_id: int, account: AccountCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    db_account = account_service.get_account_by_id(db, account_id, user.id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account_service.update_account(db, db_account, account)

@router.delete("/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = get_user_by_email(db, current_user)
    account = account_service.get_account_by_id(db, account_id, user.id)
    if not account: 
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    account_service.delete_account(db, account)
    return {"message": "Conta deletada com sucesso"}