from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.account_model import Account
from app.schemas.account_schema import AccountCreate

# Serviço de conta bancária

# Função para obter todas as contas
def get_all_accounts(db: Session, user_id: int):
    return db.query(Account).filter(Account.user_id == user_id, Account.is_active == True).all()

def get_account_by_id(db: Session, account_id: int, user_id: int):
    return db.query(Account).filter(Account.id == account_id, Account.user_id == user_id, Account.is_active == True).first()

# Criação de conta bancária
def create_account(db: Session, account: AccountCreate, user_id: int):
    accounts = get_all_accounts(db, user_id)
    if len(accounts) >= 10:
        raise HTTPException(status_code=400, detail="Limite de 10 contas atingido")
    
    new_account = Account(
        name=account.name,
        initial_balance=account.initial_balance,
        user_id=user_id
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

# Função para editar conta bancária
def update_account(db: Session, db_account: Account, account: AccountCreate):
    db_account.name = account.name
    db_account.initial_balance = account.initial_balance
    db.commit()
    db.refresh(db_account)
    return db_account

# Função para excluir conta bancária
def delete_account(db: Session, account: Account):
    account.is_active = False
    db.commit()