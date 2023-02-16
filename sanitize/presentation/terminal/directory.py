"""
Manage all rules about directories.
"""
import sqlite3
import click
import rich
from rich.table import Table
from sanitize.datasources.database.rules import RulesGateway
from sanitize.domain.usecases.directory import ListDirectoriesRules


@click.group(name="dir")
def directory() -> None:
    """
    Manage all rules about directories.
    """


@directory.command(name="all")
def directory_all() -> None:
    """
    Get all rules defined to directories.
    """
    rules_gateway = RulesGateway(sqlite3.connect("development.db"))
    list_directories_rules = ListDirectoriesRules(rules_gateway)
    table = Table(box=None)
    table.add_column()
    table.add_column(no_wrap=True)
    table.add_column()
    for rule in list_directories_rules.execute():
        table.add_row(rule.id, rule.expression, rule.comments)
    if len(table.rows) > 0:
        rich.print(table)


@directory.command(name="create")
def directory_create() -> None:
    """
    Create a new directory rule.
    """


@directory.command(name="update")
def directory_update() -> None:
    """
    Update a existing directory rule.
    """


@directory.command(name="delete")
def directory_delete() -> None:
    """
    Delete a existing directory rule.
    """
