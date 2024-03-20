from core.config import settings

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello():
    return {"message": "Hello World"}


@router.get("/secrets")
async def get_secrets():
    return {"message": settings.secret_key}
