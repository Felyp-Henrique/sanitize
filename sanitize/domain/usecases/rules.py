"""
Manage rules to sanitize.
"""
from sanitize.core.usecase import UseCase
from sanitize.core.datasource import Persistence
from sanitize.domain.entities.rules import Rule, RuleType


class RulesListUseCase(UseCase[Rule]):
    """
    Get all rules registered.
    """

    def __init__(self, datasource: Persistence[Rule]) -> None:
        self.datasource = datasource

    def execute(self, *args, **kwargs) -> list[Rule]:
        return self.datasource.all()


class RulesCreateUseCase(UseCase[Rule]):
    """
    Create a new rule about directories.
    """

    def __init__(self, datasource: Persistence[Rule]) -> None:
        self.datasource = datasource

    def execute(self, *args, **kwargs) -> None:
        rule = Rule(**kwargs, type_=RuleType.DIRECTORY)
        assert not rule.expression is None, "Needs an expression!"
        self.datasource.create(rule)
