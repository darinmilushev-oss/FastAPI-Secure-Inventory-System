# 🚀 Secure FastAPI Inventory & User Management System

A high-performance, production-ready REST API framework built with **FastAPI**, **SQLAlchemy**, and **Docker**. This project focuses on implementing industry-standard security practices and robust data architecture.

## ✨ Key Features
- **JWT Authentication:** Full implementation of secure user authentication using JSON Web Tokens.
- **Advanced Security:** Secure password storage using **Bcrypt** hashing via Passlib—ensuring zero plain-text exposure.
- **Relational Data Modeling:** Complex database schema with One-to-Many relationships between Categories and Items using SQLAlchemy ORM.
- **Data Integrity:** Strict input validation and sanitization using Pydantic schemas to prevent injection attacks.
- **Containerization:** Fully dockerized environment for seamless deployment and scalability.
- **Automated Documentation:** Interactive API documentation (Swagger UI) available out-of-the-box.

## 🛠️ Tech Stack
- **Framework:** FastAPI (Python 3.11+)
- **Database:** SQLite & SQLAlchemy ORM
- **Security:** Jose (JWT), Passlib (Bcrypt)
- **Containerization:** Docker & Docker Compose
- **Validation:** Pydantic v2

## 🚀 Getting Started

### Using Docker (Recommended)
1. Clone the repository:
   ```bash
   git clone (https://github.com/darinmilushev-oss/FastAPI-Secure-Inventory-System.git)
   cd your-repo-name