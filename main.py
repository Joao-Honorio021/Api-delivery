import os
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Variáveis de configuração
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITMO = os.getenv("ALGORITMO")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Inicialização da aplicação
app = FastAPI()

# Contexto do Bcrypt
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login-form")
# Importação dos routers depois da criação do app e contexto
from auth_routes import auth_router
from order_routes import order_router

# Inclusão das rotas
app.include_router(auth_router)
app.include_router(order_router)

# Execução (terminal): uvicorn main:app --reload

# REST APIs:
# GET     -> Leitura
# POST    -> Criação
# PUT/PATCH -> Atualização
# DELETE  -> Exclusão
