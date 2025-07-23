# Api-delivery

API de delivery desenvolvida em Python utilizando FastAPI, com autenticação, gerenciamento de usuários e pedidos.

## Funcionalidades

- Autenticação de usuários via OAuth2 e JWT
- Criação, leitura e atualização de pedidos
- Gerenciamento de usuários
- Proteção de rotas com autenticação
- Estrutura modular utilizando routers do FastAPI

## Tecnologias Utilizadas

- Python
- FastAPI
- SQLAlchemy
- JWT (via python-jose)
- Passlib (bcrypt)
- Uvicorn
- dotenv

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Joao-Honorio021/Api-delivery.git
   cd Api-delivery
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto com:
   ```
   SECRET_KEY=uma-chave-secreta
   ALGORITMO=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Execute a aplicação:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Acesse a documentação interativa:**
   - [http://localhost:8000/docs](http://localhost:8000/docs)

## Estrutura Básica

- **main.py**: Inicialização do FastAPI e inclusão das rotas.
- **auth_routes.py**: Rotas de autenticação.
- **order_routes.py**: Rotas de pedidos.
- **dependencies.py**: Funções de autenticação, sessão e validação de token.
- **models.py**: Modelos do banco de dados.

## Requisitos

- Python 3.8+
- Variáveis de ambiente configuradas
- Dependências instaladas (ver `requirements.txt`)

## Licença

Este projeto utiliza bibliotecas open source, consulte os arquivos de licença das dependências para mais detalhes.
