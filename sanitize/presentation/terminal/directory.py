"""
PASS
"""
import click


@click.group(name="dir")
def directory() -> None:
    """
    PASS
    """


@directory.command(name="all")
def directory_all() -> None:
    """
    PASS
    """


@directory.command(name="create")
def directory_create() -> None:
    """
    PASS
    """


@directory.command(name="delete")
def directory_delete() -> None:
    """
    PASS
    """
