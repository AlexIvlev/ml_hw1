from fastapi import HTTPException


def get_model(model_name: str):
    from main import ml_models
    model = ml_models.get(model_name)
    if model is None:
        raise HTTPException(status_code=500, detail=f"Model '{model_name}' not loaded")
    return model
