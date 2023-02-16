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

    def __init__(self, id_ = 0, type_ = None, expression = None, comments = None) -> None:
        self.id =  id_
        self.type = type_
        self.expression =  expression
        self.comments =  comments

    def to_dict(self) -> dict[str, any]:
        return {
            "id": self.id,
            "type": self.type,
            "expression": self.expression,
            "comments": self.comments,
        }
