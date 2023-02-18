"""
Configure all tests here.
"""
from sanitize.core.bootstrap import get_configuration, get_database
from sanitize.datasources.persistences.rules import RulesPersistence
from tests.datasources.persistences.test_rules import *
from tests.domain.usecases.test_rules import *


conf = get_configuration('test')
database = get_database(conf.env)

RulesPersistence.create_table(database)
