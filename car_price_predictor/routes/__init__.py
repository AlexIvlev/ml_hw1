from fastapi import APIRouter
from .base import router as root_router
from .items import router as items_router

router = APIRouter()
router.include_router(root_router)
router.include_router(items_router, tags=["Items"])
