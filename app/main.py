from fastapi import FastAPI
from app.routes import users
from app.database.base import Base
from app.database.connection import engine
from app.models import user_model
from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "API funcionando"}