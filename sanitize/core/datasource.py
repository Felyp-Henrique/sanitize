"""
PASS
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar("T")


class DataSourceGateway(Generic[T], ABC):
    """
    PASS
    """

    @abstractmethod
    def all(self) -> list[T]:
        """
        PASS
        """

    @abstractmethod
    def find(self, *args, **kwargs) -> T:
        """
        PASS
        """

    @abstractmethod
    def create(self, data: T) -> any:
        """
        PASS
        """

    @abstractmethod
    def update(self, data: T) -> any:
        """
        PASS
        """

    @abstractmethod
    def delete(self, data: T) -> any:
        """
        PASS
        """
