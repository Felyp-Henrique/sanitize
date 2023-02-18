"""
Manage rules to sanitize.
"""
from sanitize.core.usecase import UseCase
from sanitize.core.datasource import Persistence
from sanitize.domain.entities.rules import Rule


class RulesListUseCase(UseCase[Rule]):
    """
    ...
    """

    def __init__(self, datasource: Persistence[Rule]) -> None:
        self.datasource = datasource

    def execute(self, *args, **kwargs) -> list[Rule]:
        return self.datasource.all()
