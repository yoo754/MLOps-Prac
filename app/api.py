from fastapi import FastAPI
from joblib import load
from .database import engine, Base
from . import models


# 앱 시작 시 테이블 자동 생성
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return "h"


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}