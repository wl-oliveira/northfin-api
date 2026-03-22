# NorthFin API 💰

[🇧🇷 Português](README.pt-br.md) | 🇺🇸 English

A personal finance management REST API built with FastAPI and Python. The system allows users to control their income, expenses, bank accounts, categories and debts — with automatic balance updates on every transaction.

---

## 🚀 Features

- **Authentication** — user registration and login with JWT tokens
- **Bank Accounts** — create and manage multiple accounts with automatic balance tracking
- **Categories** — default categories on signup + custom categories per user
- **Transactions** — income and expense recording with automatic balance updates
- **Debts** — debt tracking with installment support and interest rates
- **Security** — bcrypt password hashing, JWT authentication, route protection and data isolation per user
- **Soft Delete** — records are never permanently deleted, ensuring data integrity

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Programming language |
| FastAPI | Web framework |
| SQLAlchemy | ORM |
| SQLite | Database (development) |
| Alembic | Database migrations |
| JWT (python-jose) | Authentication |
| bcrypt (passlib) | Password hashing |
| Pydantic v2 | Data validation |
| Uvicorn | ASGI server |

---

## 📁 Project Structure

```
northfin-api/
├── app/
│   ├── core/
│   │   ├── config.py        # Environment settings
│   │   └── security.py      # JWT and password utilities
│   ├── database/
│   │   ├── base.py          # SQLAlchemy base
│   │   └── connection.py    # Database connection and session
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
├── alembic/                 # Database migrations
├── .env                     # Environment variables (not versioned)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/wl-oliveira/northfin-api.git
cd northfin-api

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///./database.db
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Running the application

```bash
# Apply migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

Access the interactive API documentation at: `http://127.0.0.1:8000/docs`

---

## 📌 API Endpoints

### Auth
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | /auth/login | User login | ❌ |

### Users
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | /users/ | Create user | ❌ |
| GET | /users/ | List users | ✅ |
| GET | /users/{id} | Get user | ✅ |
| PUT | /users/{id} | Update user | ✅ |
| DELETE | /users/{id} | Delete user | ✅ |

### Accounts
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | /accounts/ | Create account | ✅ |
| GET | /accounts/ | List accounts | ✅ |
| GET | /accounts/{id} | Get account | ✅ |
| PUT | /accounts/{id} | Update account | ✅ |
| DELETE | /accounts/{id} | Delete account | ✅ |

### Categories
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | /categories/ | Create category | ✅ |
| GET | /categories/ | List categories | ✅ |
| GET | /categories/{id} | Get category | ✅ |
| PUT | /categories/{id} | Update category | ✅ |
| DELETE | /categories/{id} | Delete category | ✅ |

### Transactions
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | /transactions/ | Create transaction | ✅ |
| GET | /transactions/ | List transactions | ✅ |
| GET | /transactions/{id} | Get transaction | ✅ |
| DELETE | /transactions/{id} | Delete transaction | ✅ |

### Debts
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | /debts/ | Create debt | ✅ |
| GET | /debts/ | List debts | ✅ |
| GET | /debts/{id} | Get debt | ✅ |
| PUT | /debts/{id} | Update debt | ✅ |
| DELETE | /debts/{id} | Delete debt | ✅ |

---

## 🔒 Security

- Passwords are hashed with **bcrypt**
- Authentication via **JWT Bearer tokens**
- All sensitive routes require a valid token
- Data is isolated per user — users can only access their own data
- Sensitive configuration stored in environment variables

---

## 🗺️ Roadmap

- [ ] Rate limiting on login route
- [ ] Automated tests with pytest
- [ ] Financial reports by category and period
- [x] Debt tracking module
- [ ] Investment tracking module
- [ ] Financial goals module
- [ ] PostgreSQL support for production
- [ ] Docker containerization
- [ ] React frontend

---

## 👨‍💻 About the Author

**Washington Luís de Oliveira Júnior**

Systems Analysis and Development student at FIAP (Faculdade de Informática e Administração Paulista) and CS50 student at Harvard/edX. Passionate about backend development and cybersecurity.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/washington-olivjr)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wl-oliveira)
