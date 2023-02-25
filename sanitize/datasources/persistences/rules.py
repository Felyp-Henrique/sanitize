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
            rules.id as id_,
            rules.type as type_,
            rules.expression,
            rules.comment
        from
            rules
    """

    QUERY_FIND = """
        select
            rules.id as id_,
            rules.type as type_,
            rules.expression,
            rules.comment
        from
            rules
    """

    QUERY_CREATE = """
        insert into rules (
            type,
            expression,
            comment
        ) values (
            :type,
            :expression,
            :comment
        )
    """

    QUERY_UPDATE = """
        update rules set
            id = :id,
            type = :type,
            expression = :expression,
            comment = :comment
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
            id integer primary key autoincrement,
            type varchar(25) not null,
            expression varchar(250) not null,
            comment text
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
            return Rule() or None

    def create(self, data: Rule) -> None:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_CREATE, {
                "type": data.type.value,
                "expression": data.expression,
                "comment": data.comment
            })
            self.connection.commit()
        return None

    def update(self, data: Rule) -> None:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_UPDATE, {
                "id": data.id_,
                "type": data.type,
                "expression": data.expression,
                "comment": data.comment
            })
            self.connection.commit()
        return None

    def delete(self, data: Rule) -> None:
        with contextlib.closing(self.connection.cursor()) as cursor:
            cursor.execute(self.QUERY_DELETE, { "id": data.id_ })
            self.connection.commit()
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
