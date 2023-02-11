"""
PASS
"""
import click
import uvicorn
from fastapi import FastAPI, APIRouter
from sanitize.presentation.controllers import signin, signout, status


@click.command(name="server")
@click.option("-p", "--port", default=8080, show_default=True)
@click.option("-h", "--host", default="localhost", show_default=True)
def server(port: int, host: str) -> None:
    """
    PASS
    """
    app = FastAPI()
    router = APIRouter(prefix="/v1")
    signin.signin_controller(router)
    signout.signout_controller(router)
    status.status_controller(router)
    app.include_router(router)
    uvicorn.run(app=app, host=host, port=port)
