"""
PASS
"""
from abc import ABC, abstractmethod


class ToDict(ABC):
    """
    PASS
    """

    @abstractmethod
    def to_dict(self) -> dict[str, any]:
        """
        PASS
        """
