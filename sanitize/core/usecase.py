"""
PASS
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar("T")


class UseCase(Generic[T], ABC):
    """
    PASS
    """

    @abstractmethod
    def execute(self, *args, **kwargs) -> T | None:
        """
        PASS
        """
