from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.transaction_model import Transaction
from app.models.account_model import Account
from app.models.category_model import Category
from app.schemas.transaction_schema import TransactionCreate


def get_all_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(
        Transaction.user_id == user_id,
        Transaction.is_active == True
    ).all()


def get_transaction_by_id(db: Session, transaction_id: int, user_id: int):
    return db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user_id,
        Transaction.is_active == True
    ).first()


def create_transaction(db: Session, transaction: TransactionCreate, user_id: int):
    account = db.query(Account).filter(
        Account.id == transaction.account_id,
        Account.user_id == user_id,
        Account.is_active == True
    ).first()
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    category = db.query(Category).filter(
        Category.id == transaction.category_id,
        Category.user_id == user_id,
        Category.is_active == True
    ).first()
    if not category:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    new_transaction = Transaction(
        type=transaction.type,
        amount=transaction.amount,
        description=transaction.description,
        date=transaction.date,
        category_id=transaction.category_id,
        account_id=transaction.account_id,
        user_id=user_id
    )
    db.add(new_transaction)

    if transaction.type == "income":
        account.current_balance += transaction.amount
    else:
        account.current_balance -= transaction.amount

    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def delete_transaction(db: Session, transaction: Transaction):
    account = db.query(Account).filter(
        Account.id == transaction.account_id,
        Account.is_active == True
    ).first()
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if transaction.type == "income":
        account.current_balance -= transaction.amount
    else:
        account.current_balance += transaction.amount

    transaction.is_active = False
    db.commit()
