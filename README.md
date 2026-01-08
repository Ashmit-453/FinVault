# 🚀 FinVault — Digital Banking Backend API

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)  
[![DRF](https://img.shields.io/badge/DRF-3.15-blueviolet)](https://www.django-rest-framework.org/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)  
[![Docker](https://img.shields.io/badge/Docker-20.10-blue?logo=docker)](https://www.docker.com/)  
[![Celery](https://img.shields.io/badge/Celery-5.3-orange)](https://docs.celeryq.dev/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

FinVault is a **production-grade digital banking backend** built with Django and DRF. It supports KYC verification, secure transactions, asynchronous operations, and is fully containerized for modern deployment.

---
## 🖥️ System Design
<img width="7698" height="5786" alt="System Architecture" src="https://github.com/user-attachments/assets/fa4bcbae-360d-4318-a642-e97ac610a033" />

## 🌟 Features

- Digital Banking APIs: Deposits, withdrawals, transfers, and account management  
- KYC Verification: Document upload, validation, approvals, and audit logs  
- ACID-Compliant Transactions: Secure and consistent financial operations  
- Async Operations: Emails, media uploads, and PDF statements via Celery + RabbitMQ  
- Containerized Deployment: Docker Compose setup with NGINX reverse proxy  

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django, Django REST Framework (DRF) |
| Database | PostgreSQL |
| Task Queue | Celery + RabbitMQ |
| Web Server | NGINX |
| Containerization | Docker, Docker Compose |

---

## ⚡ Quick Start

### Prerequisites
- Docker & Docker Compose  
- Python 3.10+  
- PostgreSQL  

### Steps

1. **Clone the repository**  
`git clone https://github.com/Ashmit-453/FinVault.git && cd api`  
Clone the repository to your local machine and navigate into the project directory.

2. **Set up environment variables**  
`cp .env.example .env`  
Copy the example environment file and rename it to `.env`.  
Then update it with your database credentials, secret keys, and any other required configuration.

3. **Build and start services**  
`docker compose -f local.yml up --build -d --remove-orphans`  
Use Docker Compose to build all required services (API, PostgreSQL, RabbitMQ, etc.) and start them.

4. **Run database migrations**  
`docker compose -f local.yml run --rm api python manage.py migrate`  
Apply all Django database migrations to set up your PostgreSQL schema.

5. **Create a superuser (optional)**  
`docker compose run --rm api python manage.py createsuperuser`  
Create a superuser account to access the Django admin panel.

6. **Collect static files (if needed)**  
`docker compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear`  
Collect static files so assets are served correctly in production.

7. **Access the API**  
Open your browser or API client and navigate to:  
`http://localhost:8080/api/`  
This is the base URL for the API.

8. **Stop services**  
`docker compose -f local.yml down`  
Stop all running Docker containers while preserving your database data in Docker volumes.

---

## 📝 Celery Tasks

- Emails: Transaction notifications, welcome emails,  
- Media Uploads: Profile pictures & KYC documents  
- PDF Statements: Generate account statements  

---

## 📌 API Endpoints 

- `POST /api/v1/auth/users/` — User registration  
- `POST /api/v1/auth/login/` — User login
- `POST /api/v1/auth/verify-otp/` — otp verification
- `POST /api/v1/auth/users/activation/`- account activation
- `POST /api/v1/profiles/my-profile/`- KYC upload
- `POST /api/v1/accounts/deposit/` — Deposit money  
- `POST /api/v1/accounts/initiate-withdrawal/` — Withdraw money  
- `POST /api/v1/accounts/transfer/initiate/` — Transfer funds    
- `GET /api/v1/accounts/transactions/` — Transaction history  

> Full API documentation is available via **DRF browsable API** or Swagger if configured.

---

## 🚀 Deployment

- Configure **NGINX** as a reverse proxy  
- Use **Docker Compose** for multi-service deployment  
- Recommended: HTTPS via Let's Encrypt  

---

## 👨‍💻 Author

**Ashmit Pandey** — Backend Developer  
[GitHub](https://github.com/ashmit-453) | [LinkedIn](https://www.linkedin.com/in/ashmit-pandey/)
