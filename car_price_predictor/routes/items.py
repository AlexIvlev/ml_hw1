import io

import numpy as np
from fastapi import HTTPException, File, UploadFile, APIRouter, status
from fastapi.responses import StreamingResponse
import pandas as pd

from preprocessors import preprocess_item
from schemas import Item, PredictionResponse
from utils.model import get_model
from validators.csv import validate_csv

router = APIRouter()


@router.post("/predict_item", response_model=PredictionResponse)
def predict_item(item: Item):
    try:
        item_dict = item.dict()

        preprocessed_df = preprocess_item(item_dict)

        model = get_model("ridge_regressor")

        prediction = model.predict(preprocessed_df)[0]
        prediction_exp = round(np.expm1(prediction), 2)

        return PredictionResponse(
            prediction=prediction_exp
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Prediction failed: {str(e)}")


@router.post("/predict_items", response_model=list[PredictionResponse])
def predict_items(items: list[Item]):
    try:
        items_dict = [item.dict() for item in items]

        preprocessed_df = pd.concat([preprocess_item(item) for item in items_dict], ignore_index=True)

        model = get_model("ridge_regressor")

        predictions = model.predict(preprocessed_df)
        predictions_exp = [round(np.expm1(prediction), 2) for prediction in predictions]

        return [PredictionResponse(prediction=prediction) for prediction in predictions_exp]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Prediction failed: {str(e)}")


@router.post("/predict_items_csv")
async def predict_items_csv(file: UploadFile = File(...)) -> StreamingResponse:
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        validate_csv(df)

        preprocessed_df = pd.concat([preprocess_item(row) for _, row in df.iterrows()], ignore_index=True)

        model = get_model("ridge_regressor")

        predictions = model.predict(preprocessed_df)
        predictions_exp = [round(np.expm1(prediction), 2) for prediction in predictions]

        df["predicted_price"] = predictions_exp

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error occurred: {str(e)}")

    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predicted_items.csv"}
    )
