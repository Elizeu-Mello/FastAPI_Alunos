# API de Alunos - FastAPI

Este projeto é uma API CRUD simples para gerenciar informações de alunos. Esta API foi desenvolvida utilizando [FastAPI](https://fastapi.tiangolo.com/)

*Ele foi construído usando as seguites tecnologias:*
- **FastAPI:** Framework moderno para construir APIs web em Python.
- **SQLAlchemy:** ORM para facilitar a interação com o banco de dados.
- **PostgreSQL:** Banco de dados relacional.
- **Uvicorn:** Servidor ASGI para execução da aplicação FastAPI.
  
## Funcionalidades

- **Criar Aluno:** Adicionar um novo aluno ao banco de dados.
- **Listar Alunos:** Obter uma lista de alunos com paginação.
- **Obter Aluno por ID:** Recuperar os detalhes de um aluno específico.
- **Atualizar Aluno:** Atualizar os dados de um aluno existente.
- **Excluir Aluno:** Remover um aluno da base de dados.

    ## Estrutura do Projeto
    -   ├── alunos_api/
    -   │   ├── venv/                # Ambiente virtual
    -   │   ├── __init__.py
    -   │   ├── main.py              # Arquivo principal da API
    -   │   ├── models.py            # Modelos para o banco de dados
    -   │   ├── crud.py              # Operações CRUD com o banco de dados
    -   │   ├── database.py          # Configuração do banco de dados
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
Define os endpoints da API e integra as funções de CRUD:

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
### Pré-requisitos

- [Python 3.12](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
---
## Instalação
Siga as etapas abaixo para configurar e rodar o projeto localmente.

### 1.1. Crie um ambiente virtual na pasta do projeto
```
python -m venv [nome do ambiente]
venv\Scripts\activate.ps1 #ativa o ambiente 
```
### 1.2. Instale as dependências
Instale os pacotes necessários com o pip. ` O Pip geralmente vem junto com o Python`
```
pip install fastapi uvicorn sqlalchemy psycopg2
```
### Passo 2: Configurando o Banco de Dados PostgreSQL

2.1. Configurando a conexão no projeto

- No arquivo [database.py](https://github.com/Elizeu-Mello/FastAPI_Alunos/blob/main/database.py) você vai configurar a conexão do banco de dados:
    - `SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/universidade_db"`
 
### 3.0 Executar o Projeto
  Para executar o projeto, utilize o Uvicorn:
```
  uvicorn main:app --reload
```
### Acesse o endereço no navegador:
- http://127.0.0.1:8000

### Acesse a documentação automática do FastAPI:
- http://127.0.0.1:8000/docs
