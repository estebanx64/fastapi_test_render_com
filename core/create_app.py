from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import hello
from core.config import Settings


def add_middleware(app: FastAPI) -> None:
    """Add middlewares for the app instance

    @param app: FastAPI app instance
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def add_routers(app: FastAPI) -> None:
    """Add the routers applications for the app

    @param app: FastAPI app instance
    """

    app.include_router(hello.router, prefix="/v1")


def add_exception_handlers(app: FastAPI) -> None:
    """Add exceptions global handlers to catch errors in app

    @param app: FastAPI app instance
    """

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        )


def init_app(settings: Settings) -> FastAPI:
    """Init app and its components and return and FastAPI instance

    @param settings: Pydantic BaseSettings Model with mongo uri, driver, db_name, etc
    """
    app = FastAPI()
    add_middleware(app)
    add_routers(app)
    add_exception_handlers(app)
    return app
