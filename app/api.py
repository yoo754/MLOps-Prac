from pathlib import Path
import numpy as np
from fastapi import FastAPI, Response
from joblib import load
from .schemas import Wine, Rating, feature_names


app = FastAPI()


@app.get("/")
def root():
    return "Wine Quality Ratings"


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}