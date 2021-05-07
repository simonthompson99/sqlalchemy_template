"""
testing the basic operation of the databases
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

    def testInsert(self):

        a = db_a.TableOne(col_a = 'Peter')

        self.s.add(a)

        self.s.commit()
