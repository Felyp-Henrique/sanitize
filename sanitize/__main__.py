"""
PASS
"""
import click
from sanitize.core.bootstrap import get_configuration, get_database
from sanitize.datasources.persistences.rules import RulesPersistence
from sanitize.presentation.commands import configuration
from sanitize.presentation.commands import directory
from sanitize.presentation.commands import server
from sanitize.presentation.commands import shell


conf = get_configuration()
database = get_database(conf.env)


@click.group()
def app():
    """
    Entrypoint to application.
    """


@app.command("version")
def app_version():
    """
    Application version.
    """
    click.echo("0.1.0")


RulesPersistence.create_table(database)


app.add_command(configuration.configuration)
app.add_command(directory.directory)
app.add_command(server.server)
app.add_command(shell.shell)
app()
