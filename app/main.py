from fastapi import FastAPI
from app.routes import users, auth, accounts
from app.database.base import Base
from app.database.connection import engine
from app.models import user_model, account_model

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NorthFin API",
    description = "API de controle financeiro pessoal",
    version = "0.1.0"
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(accounts.router)

@app.get("/")
def home():
    return {"message": "NorthFin API funcionando"}