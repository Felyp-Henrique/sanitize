"""
PASS
"""
from fastapi import APIRouter


def signout_controller(router: APIRouter) -> None:
    """
    PASS
    """

    @router.post("/signout")
    def signout():
        """
        PASS
        """
        return { "data": "OK!", "status": 200, "errors": [] }
