from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, database
from .database import engine

# Cria todas as tabelas no banco de dados, se elas ainda não existirem,
# com base nas definições de modelos do SQLAlchemy.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rota para a página inicial Utilizando Método HTTP: GET
@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de Alunos!"}


# Criação de um Aluno | Método HTTP: POST
# Recebe os parâmetros 'nome' e 'email' diretamente da solicitação.
# A sessão do banco de dados é passada com 'Depends'.
@app.post("/alunos/")
def create_aluno(nome: str, email: str, db: Session = Depends(database.get_db)):
    return crud.create_aluno(db=db, nome=nome, email=email)

# Listagem de Alunos | Método HTTP: GET
# Permite a paginação com os parâmetros 'skip' e 'limit'.
@app.get("/alunos/")
def read_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    alunos = crud.get_alunos(db, skip=skip, limit=limit)
    return alunos

# Obter Aluno por ID | Método HTTP: GET
# Verifica se o aluno existe no banco de dados e retorna os dados do aluno.
@app.get("/alunos/{aluno_id}")
def read_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = crud.get_aluno(db, aluno_id=aluno_id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return aluno

# Atualizar os dados do Aluno | Método HTTP: PUT
# Recebe o ID do aluno, além dos novos valores de 'nome' e 'email' que serão atualizados.
@app.put("/alunos/{aluno_id}")
def update_aluno(aluno_id: int, nome: str, email: str, db: Session = Depends(database.get_db)):
    aluno = crud.update_aluno(db=db, aluno_id=aluno_id, nome=nome, email=email)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return aluno

# Excluir Aluno do banco de dados. | Método HTTP: DELETE
# Recebe o ID do aluno e tenta excluir o registro correspondente.
@app.delete("/alunos/{aluno_id}")
def delete_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    result = crud.delete_aluno(db=db, aluno_id=aluno_id)
    if not result:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return {"message": "Aluno deleted successfully"} 
# Em casos de erros, como um aluno não encontrado, exceções HTTP apropriadas são levantadas, como a HTTPException com código de status 404.
