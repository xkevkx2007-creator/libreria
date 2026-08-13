# 📚 Sistema de Biblioteca

Sistema web para gestionar una biblioteca, desarrollado con **Python, FastAPI, MySQL, HTML, CSS y JavaScript**.

El proyecto permite realizar las operaciones principales de gestión de libros mediante una API REST conectada a una base de datos MySQL.

---

## 🚀 Tecnologías utilizadas

### Backend
- Python
- FastAPI
- Pydantic
- MySQL Connector
- Uvicorn

### Base de datos
- MySQL
- MySQL Workbench

### Frontend
- HTML5
- CSS3
- JavaScript
- Fetch API

---

## 🏗️ Arquitectura

El proyecto utiliza una arquitectura básica de cliente-servidor:

```text
┌──────────────────────┐
│      FRONTEND        │
│  HTML + CSS + JS     │
└──────────┬───────────┘
           │
           │ HTTP / JSON
           ▼
┌──────────────────────┐
│       BACKEND        │
│       FastAPI        │
│       Python         │
└──────────┬───────────┘
           │
           │ SQL
           ▼
┌──────────────────────┐
│      DATABASE        │
│        MySQL         │
└──────────────────────┘
