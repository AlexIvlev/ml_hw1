import pandas as pd
from fastapi import HTTPException, status

from schemas import Item


def validate_csv(df: pd.DataFrame):
    items_data = df.to_dict(orient="records")
    validated_items = []

    for item_data in items_data:
        try:
            validated_item = Item(**item_data)
            validated_items.append(validated_item)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Validation error in row: {item_data}. Error: {str(e)}"
            )

    return validated_items
