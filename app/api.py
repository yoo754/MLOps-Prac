from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os

# DB 연결
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@postgres:5432/mydatabase")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 모델 정의
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

app = FastAPI()

# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 엔드포인트
@app.get("/")
def root():
    return {"message": "PostgreSQL Connected!"}

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": user.id, "name": user.name, "email": user.email} for user in users]

@app.get("/users/count")
def count_users(db: Session = Depends(get_db)):
    count = db.query(User).count()
    return {"total_users": count}
