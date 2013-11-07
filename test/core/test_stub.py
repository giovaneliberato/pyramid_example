import unittest
from core import connection_factory
from pymongo import Connection


def create_mock_collection():
    c = Connection()
    return c['temp_db']


class MongoTestCase(unittest.TestCase):
    def setUp(self):
        connection_factory.create = create_mock_collection

    def tearDown(self):
        Connection().drop_database('temp_db')
