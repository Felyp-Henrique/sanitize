"""
PASS
"""
import click
from sanitize.core.bootstrap import get_configuration, get_database
from sanitize.datasources.persistences.rules import RulesPersistence
from sanitize.presentation.terminal import configuration
from sanitize.presentation.terminal import directory
from sanitize.presentation.terminal import server


conf = get_configuration()
database = get_database(conf.env)


@click.group()
def app():
    """
    PASS
    """


RulesPersistence.create_table(database)


app.add_command(configuration.configuration)
app.add_command(directory.directory)
app.add_command(server.server)
app()
