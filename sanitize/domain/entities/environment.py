"""
Define entities to configuration environments.
"""
from os import path
from pathlib import Path


HOME_PATH = Path.home()
HOME_SANITIZE = path.join(HOME_PATH, '.sanitize')


class Environment:
    """
    Application environment configuration.
    """

    def __init__(self, home = HOME_SANITIZE, env = "development") -> None:
        self.home = home
        self.env = env

    @staticmethod
    def create(env: str) -> object:
        """
        Create a new test environment.

        Args:
            env (str): development, test or production

        Returns:
            object: Return a Enviroment instance.
        """
        return Environment(env = env)
