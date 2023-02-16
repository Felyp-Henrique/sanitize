"""
PASS
"""
from sanitize.core.usecase import UseCase
from sanitize.core.datasource import DataSourceGateway
from sanitize.domain.entities.rules import Rule


class ListDirectoriesRules(UseCase[any]):
    """
    PASS
    """

    def __init__(self, datasource: DataSourceGateway[Rule]) -> None:
        self.datasource = datasource

    def execute(self, *args, **kwargs) -> list[Rule]:
        return [rule.to_dict() for rule in self.datasource.all()]


class CreateDirectoriesRules(UseCase[any]):
    """
    PASS
    """

    def __init__(self, datasource: DataSourceGateway[Rule]) -> None:
        self.datasource = datasource

    def execute(self, *args, **kwargs) -> any:
        return None


class UpdateDirectoriesRules(UseCase[any]):
    """
    PASS
    """

    def __init__(self, datasource: DataSourceGateway[Rule]) -> None:
        self.datasource = datasource

    def execute(self, *args, **kwargs) -> any:
        return None


class DeleteDirectoriesRules(UseCase[any]):
    """
    PASS
    """

    def __init__(self, datasource: DataSourceGateway[Rule]) -> None:
        self.datasource = datasource

    def execute(self, *args, **kwargs) -> any:
        return None
