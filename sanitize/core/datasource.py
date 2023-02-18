"""
Bases to create interaction with data in external data sources.
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar("T")


class Persistence(Generic[T], ABC):
    """
    Class base to persistence in database.
    """

    @abstractmethod
    def all(self) -> list[T]:
        """
        Get all registers.
        """

    @abstractmethod
    def find(self, *args, **kwargs) -> T:
        """
        Find only one register in database.
        """

    @abstractmethod
    def create(self, data: T) -> any:
        """
        Create a new register in database.
        """

    @abstractmethod
    def update(self, data: T) -> any:
        """
        Update a existing register in database.
        """

    @abstractmethod
    def delete(self, data: T) -> any:
        """
        Delete a existing register in database.
        """
