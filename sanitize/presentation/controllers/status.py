"""
PASS
"""
from fastapi import APIRouter


def status_controller(router: APIRouter) -> None:
    """
    PASS
    """

    @router.get("/status")
    def status():
        """
        PASS
        """
        return { "data": "OK!", "status": 200, "errors": [] }
