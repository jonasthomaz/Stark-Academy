from fastapi import APIRouter, status
from .balance import balance_router

default_router = APIRouter(tags=["default", "healthcheck"])


@default_router.get("/", status_code=status.HTTP_200_OK)
async def home():
    return "Stark Academy"


routes = (default_router, balance_router)
