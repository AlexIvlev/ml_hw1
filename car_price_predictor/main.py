import pickle
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from routes import router

MODEL_DIR = "models"
MODEL_NAME = "ridge_reg_model.pkl"

ml_models = {}


@asynccontextmanager
async def ml_lifespan_manager(app: FastAPI):
    model_path = Path(MODEL_DIR) / MODEL_NAME
    try:
        with open(model_path, "rb") as pkl:
            ml_models["ridge_regressor"] = pickle.load(pkl)
        yield
    finally:
        ml_models.clear()

app = FastAPI(lifespan=ml_lifespan_manager)
app.include_router(router)
