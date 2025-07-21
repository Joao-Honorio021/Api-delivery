from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao , verificar_token
from schemas import PedidoSchema
from models import Pedido , Usuario


order_router = APIRouter(prefix="/pedidos", tags=["pedidos"],dependecies = Depends(verificar_token))

@order_router.get("/")
async def pedidos():
    
    return {"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}

@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao),usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not  usuario.admin or  usuario.id != pedido.usuario:
        raise HTTPException(status_code=403, detail="Acesso negado. Apenas administradores podem cancelar pedidos.")
    pedido.status = "CANCELADO"
    session.commit()
    return {"mensagem": f"Pedido {id_pedido} cancelado com sucesso",
    "pedido": pedido
    }
@order_router.get("/pedido/admin/listar", response_model=list[PedidoSchema])
async def listar_pedidos_admin(
    session: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(verificar_token)
):
    if not usuario.admin:
        raise HTTPException(status_code=403, detail="Acesso negado. Apenas administradores podem listar pedidos.")

    pedidos = session.query(Pedido).all()
    return pedidos
