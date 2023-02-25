"""
Interactive commands to test and run actions.
"""
import click
from sanitize.presentation.terminal.terminal import Terminal


@click.command(name="shell")
def shell():
    """
    Run interactive mode.
    """
    terminal = Terminal()
    terminal.cmdloop()
