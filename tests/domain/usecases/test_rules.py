"""
Unit test to Rules Use Case
"""
import unittest
from unittest.mock import Mock
from faker import Faker
from sanitize.domain.entities.rules import Rule, RuleType
from sanitize.domain.usecases.rules import RulesListUseCase


class TestRulesListUseCase(unittest.TestCase):
    """
    Unit test to Rules List Use Case
    """

    def test_list_all(self):
        """
        Check if all rules is getting to right
        """
        rules = [self.get_rule() for _ in range(0, 10)]
        persistence = Mock()
        persistence.all.return_value = rules
        usecase = RulesListUseCase(persistence)
        result = usecase.execute()
        self.assertEqual(len(result), 10)
        for rule_result, rule_expected in zip(result, rules):
            self.assertEqual(rule_result.id_, rule_expected.id_)
            self.assertEqual(rule_result.type, rule_expected.type)
            self.assertEqual(rule_result.expression, rule_expected.expression)
            self.assertEqual(rule_result.comments, rule_expected.comments)

    @staticmethod
    def get_rule() -> Rule:
        """
        Generate fake rule
        """
        faker = Faker()
        return Rule(
            id_=faker.random.randint(1, 999),
            type_=faker.random.choice([RuleType.DIRECTORY]),
            expression=faker.file_path(depth=3),
            comments=faker.sentence(nb_words=10),
        )
