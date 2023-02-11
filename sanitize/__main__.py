"""
PASS
"""
import click
from sanitize.presentation.terminal import directory
from sanitize.presentation.terminal import server


@click.group()
def app():
    """
    PASS
    """


app.add_command(directory.directory)
app.add_command(server.server)
app()
