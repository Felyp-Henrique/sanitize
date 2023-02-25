"""
PASS
"""
from enum import Enum
from sanitize.core.serialize import ToDict


class RuleType(Enum):
    """
    PASS
    """
    DIRECTORY = "directory"

    def is_directory(self) -> bool:
        """
        PASS
        """
        return self.name == self.DIRECTORY.name


class Rule(ToDict):
    """
    PASS
    """

    def __init__(self, id_ = 0, type_ = None, expression = None, comment = None) -> None:
        self.id_ =  id_
        self.type = type_
        self.expression =  expression
        self.comment =  comment

    def to_dict(self) -> dict[str, any]:
        return {
            "id": self.id_,
            "type": self.type,
            "expression": self.expression,
            "comments": self.comment,
        }
