from models import db, Usuario
from main import SECRET_KEY, ALGORITMO, oauth2_scheme
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends, HTTPException
from jose import jwt, JWTError

SessionLocal = sessionmaker(bind=db)

def pegar_sessao():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def verificar_token(token: str = Depends(oauth2_scheme), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return usuario
