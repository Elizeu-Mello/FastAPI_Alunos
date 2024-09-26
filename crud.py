from sqlalchemy.orm import Session
from . import models

def get_aluno(db: Session, aluno_id: int):
    return db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

def get_alunos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Aluno).offset(skip).limit(limit).all()

def create_aluno(db: Session, nome: str, email: str):
    db_aluno = models.Aluno(nome=nome, email=email)
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def update_aluno(db: Session, aluno_id: int, nome: str, email: str):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if aluno:
        aluno.nome = nome
        aluno.email = email
        db.commit()
        db.refresh(aluno)
        return aluno
    return None

def delete_aluno(db: Session, aluno_id: int):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if aluno:
        db.delete(aluno)
        db.commit()
        return True
    return False
