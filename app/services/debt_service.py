from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.debt_model import Debt
from app.schemas.debt_schema import DebtCreate

def get_all_debts(db: Session, user_id: int):
    return db.query(Debt).filter(
        Debt.user_id == user_id,
        Debt.is_active == True
    ).all()

def get_debt_by_id(db: Session, debt_id: int, user_id: int):
    return db.query(Debt).filter(
        Debt.id == debt_id,
        Debt.user_id == user_id,
        Debt.is_active == True
    ).first()

def create_debt(db: Session, debt: DebtCreate, user_id: int):
    new_debt = Debt (
        name = debt.name,
        total_amount = debt.total_amount,
        interest_rate = debt.interest_rate,
        status = debt.status,
        due_date = debt.due_date,
        is_installment = debt.is_installment,
        total_installments = debt.total_installments,
        remaining_installments = debt.total_installments,
        account_id = debt.account_id,
        user_id = user_id
    )
    db.add(new_debt)
    db.commit()
    db.refresh(new_debt)
    return new_debt

def update_debt(db: Session, db_debt: Debt, debt: DebtCreate):
    db_debt.name = debt.name
    db_debt.due_date = debt.due_date
    db_debt.total_amount = debt.total_amount
    db_debt.interest_rate = debt.interest_rate
    db_debt.total_installments = debt.total_installments
    db_debt.is_installment = debt.is_installment
    db_debt.status = debt.status
    db.commit()
    db.refresh(db_debt)
    return db_debt

def delete_debt(db: Session, debt: Debt):
    debt.is_active = False
    db.commit()
