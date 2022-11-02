from fastapi import FastAPI
from starkacademy.router import routes


def create_app() -> FastAPI:
    current_app = FastAPI(
        title="Stark Academy",
        version="0.0.1"
    )

    for route in routes:
        current_app.include_router(route)
