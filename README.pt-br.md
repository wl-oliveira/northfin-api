# NorthFin API 💰

🇧🇷 Português | [🇺🇸 English](README.md)

Uma API REST de controle financeiro pessoal desenvolvida com FastAPI e Python. O sistema permite que usuários controlem suas receitas, despesas, contas bancárias, categorias e dívidas — com atualização automática de saldo a cada transação.

---

## 🚀 Funcionalidades

- **Autenticação** — cadastro e login de usuários com tokens JWT
- **Contas Bancárias** — criação e gerenciamento de múltiplas contas com controle automático de saldo
- **Categorias** — categorias padrão criadas no cadastro + categorias personalizadas por usuário
- **Transações** — registro de receitas e despesas com atualização automática de saldo
- **Dívidas** — controle de dívidas com suporte a parcelamento e juros
- **Segurança** — hash de senhas com bcrypt, autenticação JWT, proteção de rotas e isolamento de dados por usuário
- **Soft Delete** — registros nunca são deletados permanentemente, garantindo integridade dos dados

---

## 🛠️ Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Linguagem de programação |
| FastAPI | Framework web |
| SQLAlchemy | ORM |
| SQLite | Banco de dados (desenvolvimento) |
| Alembic | Migrations do banco de dados |
| JWT (python-jose) | Autenticação |
| bcrypt (passlib) | Hash de senhas |
| Pydantic v2 | Validação de dados |
| Uvicorn | Servidor ASGI |

---

## 📁 Estrutura do Projeto

```
northfin-api/
├── app/
│   ├── core/
│   │   ├── config.py        # Configurações de ambiente
│   │   └── security.py      # Utilitários JWT e senha
│   ├── database/
│   │   ├── base.py          # Base do SQLAlchemy
│   │   └── connection.py    # Conexão e sessão com o banco
│   ├── models/
│   │   ├── user_model.py
│   │   ├── account_model.py
│   │   ├── category_model.py
│   │   ├── transaction_model.py
│   │   └── debt_model.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── account_schema.py
│   │   ├── category_schema.py
│   │   ├── transaction_schema.py
│   │   └── debt_schema.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── account_service.py
│   │   ├── category_service.py
│   │   ├── transaction_service.py
│   │   └── debt_service.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── accounts.py
│   │   ├── categories.py
│   │   ├── transactions.py
│   │   └── debts.py
│   └── main.py
├── alembic/                 # Migrations do banco de dados
├── .env                     # Variáveis de ambiente (não versionado)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Como Executar

### Pré-requisitos
- Python 3.11+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/wl-oliveira/northfin-api.git
cd northfin-api

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URL=sqlite:///./database.db
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Executando a aplicação

```bash
# Aplicar as migrations
alembic upgrade head

# Iniciar o servidor
uvicorn app.main:app --reload
```

Acesse a documentação interativa em: `http://127.0.0.1:8000/docs`

---

## 📌 Endpoints da API

### Auth
| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | /auth/login | Login do usuário | ❌ |

### Usuários
| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | /users/ | Criar usuário | ❌ |
| GET | /users/ | Listar usuários | ✅ |
| GET | /users/{id} | Buscar usuário | ✅ |
| PUT | /users/{id} | Atualizar usuário | ✅ |
| DELETE | /users/{id} | Deletar usuário | ✅ |

### Contas Bancárias
| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | /accounts/ | Criar conta | ✅ |
| GET | /accounts/ | Listar contas | ✅ |
| GET | /accounts/{id} | Buscar conta | ✅ |
| PUT | /accounts/{id} | Atualizar conta | ✅ |
| DELETE | /accounts/{id} | Deletar conta | ✅ |

### Categorias
| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | /categories/ | Criar categoria | ✅ |
| GET | /categories/ | Listar categorias | ✅ |
| GET | /categories/{id} | Buscar categoria | ✅ |
| PUT | /categories/{id} | Atualizar categoria | ✅ |
| DELETE | /categories/{id} | Deletar categoria | ✅ |

### Transações
| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | /transactions/ | Criar transação | ✅ |
| GET | /transactions/ | Listar transações | ✅ |
| GET | /transactions/{id} | Buscar transação | ✅ |
| DELETE | /transactions/{id} | Deletar transação | ✅ |

### Dívidas
| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | /debts/ | Criar dívida | ✅ |
| GET | /debts/ | Listar dívidas | ✅ |
| GET | /debts/{id} | Buscar dívida | ✅ |
| PUT | /debts/{id} | Atualizar dívida | ✅ |
| DELETE | /debts/{id} | Deletar dívida | ✅ |

---

## 🔒 Segurança

- Senhas protegidas com **bcrypt**
- Autenticação via **JWT Bearer tokens**
- Todas as rotas sensíveis exigem token válido
- Dados isolados por usuário — cada usuário acessa apenas os próprios dados
- Configurações sensíveis armazenadas em variáveis de ambiente

---

## 🗺️ Próximos Passos

- [ ] Rate limiting na rota de login
- [ ] Testes automatizados com pytest
- [ ] Relatórios financeiros por categoria e período
- [x] Módulo de controle de dívidas
- [ ] Módulo de controle de investimentos
- [ ] Módulo de metas financeiras
- [ ] Suporte a PostgreSQL para produção
- [ ] Containerização com Docker
- [ ] Frontend em React

---

## 👨‍💻 Sobre o Autor

**Washington Luís de Oliveira Júnior**

Estudante de Análise e Desenvolvimento de Sistemas pela FIAP (Faculdade de Informática e Administração Paulista) e aluno do CS50 da Harvard/edX. Apaixonado por desenvolvimento backend e segurança da informação.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/washington-olivjr)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wl-oliveira)
