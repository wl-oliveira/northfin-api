from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.category_model import Category
from app.schemas.category_schema import CategoryCreate

DEFAULT_CATEGORIES = [
    {"name": "Alimentação", "type": "expense"},
    {"name": "Transporte", "type": "expense"},
    {"name": "Moradia", "type": "expense"},
    {"name": "Saúde", "type": "expense"},
    {"name": "Lazer", "type": "expense"},
    {"name": "Educação", "type": "expense"},
    {"name": "Vestuário", "type": "expense"},
    {"name": "Salário", "type": "income"},
    {"name": "Freelance", "type": "income"},
    {"name": "Investimentos", "type": "income"},
    {"name": "Outros", "type": "income"},
]

def create_default_categories(db: Session, user_id: int):
    for category in DEFAULT_CATEGORIES:
        db.add(Category(
            name=category["name"],
            type=category["type"],
            is_default=True,
            user_id=user_id
        ))
    db.commit()

def get_all_categories(db: Session, user_id: int):
    return db.query(Category).filter(
        Category.user_id == user_id,
        Category.is_active == True
    ).all()

def get_category_by_id(db: Session, category_id: int, user_id: int):
    return db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == user_id,
        Category.is_active == True
    ).first()

def create_category(db: Session, category: CategoryCreate, user_id: int):
    new_category = Category(
        name=category.name,
        type=category.type,
        is_default=False,
        user_id=user_id
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def update_category(db: Session, db_category: Category, category: CategoryCreate):
    db_category.name = category.name
    db_category.type = category.type
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category: Category):
    if category.is_default:
        raise HTTPException(status_code=400, detail="Categorias padrão não podem ser deletadas")
    category.is_active = False
    db.commit()