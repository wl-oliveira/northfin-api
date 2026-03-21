from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.transaction_model import Transaction
from app.models.account_model import Account
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

    account = db.query(Account).filter(Account.id == transaction.account_id).first()
    if transaction.type == "income":
        account.current_balance += transaction.amount
    else:
        account.current_balance -= transaction.amount

    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def delete_transaction(db: Session, transaction: Transaction):
    account = db.query(Account).filter(Account.id == transaction.account_id).first()
    if transaction.type == "income":
        account.current_balance -= transaction.amount
    else:
        account.current_balance += transaction.amount

    transaction.is_active = False
    db.commit()
