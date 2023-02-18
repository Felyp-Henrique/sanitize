"""
PASS
"""
import sqlite3
import contextlib
from sanitize.core.datasource import Persistence
from sanitize.domain.entities.rules import Rule


class RulesPersistence(Persistence[Rule]):
    """
    PASS
    """

    QUERY_ALL = """
        select
            rules.id,
            rules.type,
            rules.expression,
            rules.comments
        from
            rules
    """

    QUERY_FIND = """
        select
            rules.id,
            rules.type,
            rules.expression,
            rules.comments
        from
            rules
    """

    QUERY_CREATE = """
        insert into rules (
            id,
            type,
            expression,
            comments
        ) values (
            :id,
            :type,
            :expression,
            :comments
        )
    """

    QUERY_UPDATE = """
        update rules set
            id = :id,
            type = :type,
            expression = :expression,
            comments = :comments
        where
            id = :id
    """

    QUERY_DELETE = """
        delete from
            rules
        where
            id = :id
    """

    QUERY_CREATE_TABLE = """
        create table if not exists rules (
            id int auto increment primary key,
            type varchar(25) not null,
            expression varchar(250) not null,
            comments text
        )
    """

    def __init__(self, database: sqlite3.Connection) -> None:
        self.connection = database

    def all(self) -> list[Rule]:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_ALL)
            return [Rule(*rule) for rule in cursor.fetchall()]

    def find(self, *args, **kwargs) -> Rule | None:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_FIND)
            return Rule(*cursor.fetchone()) or None

    def create(self, data: Rule) -> None:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_CREATE, {
                "id": data.id_,
                "type": data.type,
                "expression": data.expression,
                "comments": data.comments
            })
        return None

    def update(self, data: Rule) -> None:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_UPDATE, {
                "id": data.id_,
                "type": data.type,
                "expression": data.expression,
                "comments": data.comments
            })
        return None

    def delete(self, data: Rule) -> None:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_DELETE, { "id": data.id_ })
        return None

    @staticmethod
    def create_table(connection: sqlite3.Connection) -> None:
        """
        Create table "rules"

        Args:
            connection (sqlite3.Connection): Database connection
        """
        with contextlib.closing(connection.cursor()) as cursor:
            cursor.execute(RulesPersistence.QUERY_CREATE_TABLE)
