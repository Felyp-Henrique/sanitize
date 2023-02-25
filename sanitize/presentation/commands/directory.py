"""
Manage all rules about directories.
"""
import sqlite3
import click
import rich
from rich.table import Table
from sanitize.datasources.persistences.rules import RulesPersistence
from sanitize.domain.usecases.rules import RulesListUseCase, RulesCreateUseCase


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
    table = Table.grid(padding=(0, 1, 0, 0))
    table.add_row("[bold]ID", "[bold]EXPRESSION", "[bold]COMMENT")
    for rule in usecase_rules_list.execute():
        table.add_row(f"{ rule.id_ }", f"{ rule.expression }", f"{ rule.comment or '--' }")
    rich.print(table)


@directory.command(name="create")
@click.option("-c", "--comment", type=str, default=None, help="Add a comment in rule.")
@click.argument("expression", type=str, default=None)
def directory_create(comment: str, expression: str) -> None:
    """
    Create a new directory rule.
    """
    persistence_rules = RulesPersistence(sqlite3.connect("development.db"))
    usecase_rules_create = RulesCreateUseCase(persistence_rules)
    usecase_rules_create.execute(comment=comment, expression=expression)


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
