"""
Manage all rules about directories.
"""
import sqlite3
import click
import rich
from rich.table import Table
from sanitize.datasources.persistences.rules import RulesPersistence
from sanitize.domain.usecases.rules import RulesListUseCase


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
    persistence_rules = RulesPersistence(sqlite3.connect("development.db"))
    usecase_rules_list = RulesListUseCase(persistence_rules)
    table = Table(box=None)
    table.add_column()
    table.add_column(no_wrap=True)
    table.add_column()
    for rule in usecase_rules_list.execute():
        table.add_row(rule.id_, rule.expression, rule.comments)
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
