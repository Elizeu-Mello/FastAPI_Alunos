# API de Alunos - FastAPI

Este projeto é uma API CRUD para gerenciar informações de alunos. Esta API foi desenvolvida utilizando [FastAPI](https://fastapi.tiangolo.com/)

*Ele foi construído usando as seguites tecnologias:*
- **FastAPI:** Framework moderno para construir APIs web em Python.
- **SQLAlchemy:** ORM para facilitar a interação com o banco de dados.
- **PostgreSQL:** Banco de dados relacional.
- **Uvicorn:** Servidor ASGI para execução da aplicação FastAPI.
  

    ## Estrutura do Projeto
    -   ├── alunos_api/
    -   │── app/
    -   │   ├── venv/                # Ambiente virtual
    -   │   ├── __init__.py
    -   │   ├── main.py              # Arquivo principal da API
    -   │   │── models.py            # Modelos para o banco de dados
    -   │   ├── crud.py              # Operações CRUD com o banco de dados
    -   │   ├── database.py          # Configuração do banco de dados
    -   │
    -   ├── requirements.txt         # Dependencias   
    -   ├── .dockerignore            # Arquivo e pasta do ambiente virtual ignorar
    -   ├── Dockerfile               # Configuraçao Docker File
    -   └── README.md                # Documentação do projeto

      
### `crud.py`
Contém as funções responsáveis por interagir diretamente com o banco de dados, realizando as operações CRUD:

- `get_aluno(db, aluno_id)`: Retorna um aluno pelo ID.
- `get_alunos(db, skip, limit)`: Retorna uma lista de alunos, com paginação.
- `create_aluno(db, nome, email)`: Cria um novo aluno com nome e email.
- `update_aluno(db, aluno_id, nome, email)`: Atualiza as informações de um aluno pelo ID.
- `delete_aluno(db, aluno_id)`: Exclui um aluno pelo ID.

### `database.py`
Configura a conexão com o banco de dados PostgreSQL e define:

- `engine`: A conexão com o banco.
- `SessionLocal`: A sessão de banco de dados.
- `Base`: A classe base para a definição de modelos.
- `get_db()`: Um gerador que cria e finaliza a sessão de banco de dados.

### `main.py`
Contém as rotas e o ponto de entrada da aplicação FastAPI e integra as funções de CRUD:

- `GET /`: Página inicial da API.
- `POST /alunos/`: Criação de um novo aluno.
- `GET /alunos/`: Listagem de alunos com paginação.
- `GET /alunos/{aluno_id}`: Busca de aluno por ID.
- `PUT /alunos/{aluno_id}`: Atualização de um aluno por ID.
- `DELETE /alunos/{aluno_id}`: Exclusão de um aluno por ID.

### `models.py`
Define o modelo `Aluno`, que representa a tabela `alunos` no banco de dados PostgreSQL:

- `id`: Identificador único do aluno.
- `nome`: Nome do aluno.
- `email`: Email do aluno (único).
---

## Funcionalidades

- **Criar Aluno: (POST)**
    - Adicionar um novo aluno ao banco de dados.
    - Rota: /alunos/
    - Método: POST
    - Parâmetros: nome (string), email (string)
    - Resposta de Sucesso: 201 Created
      
- **Listar Alunos: (GET)**
  - Obter uma listar todos os alunos cadastrados.
  - Rota: /alunos/
  - Método: GET
  - Parâmetros: skip (int), limit (int) - usados para paginação.
  - Resposta de Sucesso: 200 OK (Retorna uma lista de alunos)

- **Obter Aluno por ID: (GET)**
  - Recuperar os detalhes de um aluno específico.
  - Rota: /alunos/{aluno_id}
  - Método: GET
  - Parâmetros: aluno_id (int)
  - Resposta de Sucesso: 200 OK (Retorna o aluno encontrado)
  - Resposta de Erro: 404 Not Found (Aluno não encontrado)
  
- **Atualizar Aluno: (PUT)**
  - Atualizar os dados de um aluno existente.
  - Rota: /alunos/{aluno_id}
  - Método: PUT
  - Parâmetros: aluno_id (int), nome (string), email (string)
  - Resposta de Sucesso: 200 OK
  - Resposta de Erro: 404 Not Found

- **Excluir Aluno:**
  - Remover um aluno da base de dados.
  - Rota: /alunos/{aluno_id}
  - Método: DELETE
  - Parâmetros: aluno_id (int)
  - Resposta de Sucesso: 200 OK (Aluno deletado com sucesso)
  - Resposta de Erro: 404 Not Found

 ---

 ## Banco de Dados
 - O banco de dados utilizado é o PostgreSQL rodando localmente na máquina do desenvolvedor.
 - Host: localhost
 - Porta: 5432
 - Nome do Banco: alunos_db
   
 #### Configuração de Conexão: A conexão com o banco de dados foi configurada em database.py, utilizando SQLAlchemy para gerenciar as transações.
  - SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/alunos_db"

## Dockerização
 A aplicação foi empacotada em um container Docker para facilitar o deploy. Abaixo está a configuração do `Dockerfile`.

Dockerfile:
```
# Use a imagem base do Python 3.12
FROM python:3.12.6

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que a aplicação irá utilizar
EXPOSE 8000

# Defina o comando para rodar o servidor Uvicorn (FastAPI)
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


```

### Acesse o endereço no navegador:
- http://localhost:8000

### Acesse a documentação automática do FastAPI:
- http://localhost:8000/docs
