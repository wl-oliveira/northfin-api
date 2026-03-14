from pydantic import BaseModel, EmailStr, Field

# Schemas para validação de dados
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(...,min_length=6, max_length=50)
    age: int
    phone: str

# Esquema para login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Esquema para resposta de usuário
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    phone: str
    is_active: bool

# Configuração para permitir a criação de objetos a partir de modelos ORM
class Config:
    from_attributes = True

# Esquema para resposta de token
class Token(BaseModel):
    access_token: str
    token_type: str