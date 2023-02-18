"""
Unit test to persistence about rules
"""
import unittest
from sanitize.core.bootstrap import get_configuration, get_database
from sanitize.datasources.persistences.rules import RulesPersistence


class TestRulesPersistence(unittest.TestCase):
    """
    PASS
    """

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.conf = get_configuration("test")
        self.connection = get_database(self.conf.env)

    def test_all(self):
        """
        PASS
        """
        persistence = RulesPersistence(self.connection)
        results = persistence.all()
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 0)

    def test_create(self):
        """
        PASS
        """
        #persistence = RulesPersistence(self.connection)
