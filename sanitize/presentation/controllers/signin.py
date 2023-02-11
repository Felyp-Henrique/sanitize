"""
PASS
"""
from fastapi import APIRouter


def signin_controller(router: APIRouter) -> None:
    """
    PASS
    """

    @router.post("/signin")
    def signin():
        """
        PASS
        """
        return { "data": "OK!", "status": 200, "errors": [] }
