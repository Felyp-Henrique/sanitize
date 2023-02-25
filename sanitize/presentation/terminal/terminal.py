"""
Interactive commands to test and run actions.
"""
import re
import cmd
import sqlite3
import rich
from rich.table import Table
from sanitize.core import argparse
from sanitize.datasources.persistences.rules import RulesPersistence
from sanitize.domain.usecases.rules import RulesListUseCase, RulesCreateUseCase


class Terminal(cmd.Cmd):
    """
    Cmd extension to work interacties modes.
    """
    DIR_COMMANDS = (
        r"^(?P<command>all)$",
        r"^(?P<command>create)\s*(?P<input>.*)$",
    )

    prompt = "(sanitize) "

    def do_dir(self, user_input: str):
        """
        List all dirs.

        Args:
            args (any): Arguments list.
        """
        for command_config in self.DIR_COMMANDS:
            command_regex = re.compile(command_config)
            command = command_regex.match(user_input.strip())
            if command is None:
                continue
            if command.group("command").lower() == "all":
                persistence_rules = RulesPersistence(sqlite3.connect("development.db"))
                usecase_rules_list = RulesListUseCase(persistence_rules)
                table = Table.grid(padding=(0, 1, 0, 0))
                table.add_row("[bold]ID", "[bold]EXPRESSION", "[bold]COMMENT")
                for rule in usecase_rules_list.execute():
                    table.add_row(
                        f"{ rule.id_ }", f"{ rule.expression }", f"{ rule.comment or '--' }")
                rich.print(table)
            elif command.group("command").lower() == "create":
                try:
                    options = argparse.ArgumentParserInline("sanitize dir create")
                    options.add_argument("-c", "--comment", type=str, default=None)
                    options.add_argument("expression", type=str, default=None)
                    inputs = command.group("input").split()
                    arguments = options.parse_args(inputs)
                    persistence_rules = RulesPersistence(sqlite3.connect("development.db"))
                    usecase_rules_create = RulesCreateUseCase(persistence_rules)
                    usecase_rules_create.execute(
                        comment=arguments.comment, expression=arguments.expression)
                except argparse.ArgumentParserInlineException:
                    pass

    def do_exit(self, _):
        """
        Exit from interactive mode.
        """
        exit(0)
