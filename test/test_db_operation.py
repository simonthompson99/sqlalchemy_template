"""
testing the basic operation of the databases

all test methods must be methods of a class inheriting from unittest.TestCase
with names beginning with test
setUp and tearDown are special methods run before and after every test
"""

import unittest
from config import TestConfig
from models import create_database, drop_database, make_session, db_a

class DBAConnections(unittest.TestCase):


    def setUp(self):

        self.c = TestConfig()

        create_database(self.c, 'db_a')

        self.s = make_session(self.c)

    def tearDown(self):

        self.s.close()

        drop_database(self.c, 'db_a')

    def test_insert(self):

        a = db_a.TableOne(col_a = 'Peter')

        self.s.add(a)

        self.s.commit()
