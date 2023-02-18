"""
Methods to initialize configurations and the application.
"""
import sqlite3
from sanitize.domain.entities.environment import Environment


def get_configuration(env: str = "development"):
    """
    Return the configuration app.
    """
    return Environment.create(env)


def get_database(env: str) -> sqlite3.Connection:
    """
    Return the database connection.
    """
    return sqlite3.connect(f"{ env }.db")
