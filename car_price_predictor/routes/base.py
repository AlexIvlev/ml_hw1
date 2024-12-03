from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict:
    return dict(
        name="Car Price Prediction Service",
        description="This is car price prediction service for HSE first machine learning homework."
    )
