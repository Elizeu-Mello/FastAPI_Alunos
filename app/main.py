from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, database
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Página inicial
@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de Alunos!"}


# Criação de um Aluno
@app.post("/alunos/")
def create_aluno(nome: str, email: str, db: Session = Depends(database.get_db)):
    return crud.create_aluno(db=db, nome=nome, email=email)

# Listagem de Alunos
@app.get("/alunos/")
def read_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    alunos = crud.get_alunos(db, skip=skip, limit=limit)
    return alunos

# Obter Aluno por ID
@app.get("/alunos/{aluno_id}")
def read_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = crud.get_aluno(db, aluno_id=aluno_id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return aluno

# Atualizar Aluno
@app.put("/alunos/{aluno_id}")
def update_aluno(aluno_id: int, nome: str, email: str, db: Session = Depends(database.get_db)):
    aluno = crud.update_aluno(db=db, aluno_id=aluno_id, nome=nome, email=email)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return aluno

# Excluir Aluno
@app.delete("/alunos/{aluno_id}")
def delete_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    result = crud.delete_aluno(db=db, aluno_id=aluno_id)
    if not result:
        raise HTTPException(status_code=404, detail="Aluno not found")
    return {"message": "Aluno deleted successfully"}
