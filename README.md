# finance_backend
Assignment of Zorvyn
# Finance Data Processing & Access Control Backend

## 🚀 Overview
This project is a backend system for managing financial records with role-based access control and dashboard analytics.

## 🛠 Tech Stack
- Django
- Django REST Framework
- JWT Authentication
- SQLite

## 🔐 Roles
- Viewer: Read-only access
- Analyst: View + dashboard insights
- Admin: Full CRUD access

## 📊 Features
- User management with roles
- Financial records CRUD
- Dashboard summary APIs
- Role-based access control
- JWT authentication

## 🔗 API Endpoints

### Auth
- POST /api/token/
- POST /api/token/refresh/

### Users
- GET/POST /api/users/

### Records
- GET/POST /api/records/

### Dashboard
- GET /api/dashboard/summary/

## ⚙️ Setup

```bash
git clone <repo-url>
cd finance-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
