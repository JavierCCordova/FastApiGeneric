#FastApiGeneric - Arquitectura Hexagonal - MongoDB - JWT

API desarrollada en **FastAPI** con un patrón **HEXAGONAL(Ports, Adapters)** 
Incluye autentificación JWT.

Estructura o esqueleto para consumo de API.


## 📁 Estructura del Proyecto
api/
├── routers/
│ ├── ocr.py
│ ├── routes.py
│ └── dependencies.py
│
├── application/
│ ├── authUseCase.py
│ └── tesseractUseCase.py
│
├── core/
│ └── config.py
│
├── domain/
│ ├── user/
│ │ ├── entities.py
│ │ └── ports.py
│ └── tesseract/
│ ├── entities.py
│ └── ports.py
│
├── infrastructure/
│ ├── adapters/
│ │ └── ocr/
│ │ └── tesseractPdfExtractor.py
│ │
│ ├── persistence/
│ │ └── mongodb/
│ │ ├── connection.py
│ │ └── userRepository.py
│ │
│ └── security/
│ ├── hasher.py
│ └── tokenService.py
│
├── main.py
├── script.py
├── .env
├── requirements.txt
└── README.md

## 🧠 Arquitectura Hexagonal

Request HTTP
│
▼
FastAPI Router (api/routers)
│
▼
UseCase (application)
│
▼
Port (domain/*/ports.py)
│
▼
Adapter (infrastructure)
│
▼
MongoDB / Tesseract / JWT

## ⚙️ Tecnologías

- Python 3.10+
- FastAPI
- MongoDB + Motor
- Pydantic
- python-jose (JWT)
- Passlib (Argon2)
- Tesseract OCR

## 🔧 Instalación

MongoDb community

- Se necesita crear una BBDD "fastapi_generic"
- Collection  "aviciiUser"

### Crear entorno virtual

bash
python3 -m venv venv
source venv/bin/activate

#  Dependencias
pip install -r requirements.txt

Creación 


# variables de entorno

MONGO_URI=mongodb://localhost:27017
DB_NAME=fastapi_generic
SECRET_KEY=supersecret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


## Ejecucion.

uvicorn main:app --reload

# Abrir
http://localhost:8000/docs

# Login 

 User 
 Pass

## Principios aplicados. 
Domain no depende de infraestructura
UseCases solo conocen Ports
Infraestructura implementa Ports
FastAPI es solo un adaptador

## Mejora
Docker
Tests con Pytest
Roles de usuario
Refresh Tokens

## Autor
Javier Córdova