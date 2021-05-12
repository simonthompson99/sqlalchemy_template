import os
from dotenv import load_dotenv
from models import db_a

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:

    # dictionary of the different database connections required, their models
    # to use and the dotenv variable for the connection string
    dbs = {
        'db_a': {'model': db_a,
                 'env_conn_str': 'DB_A_CONN_STR'},
    }

    def get_conn_str(self, db):
        # return connection string for a given db

        return self.dbs[db]['env_conn_str']

    def get_db_model(self, db):
        # return the model for a given db

        return self.dbs[db]['model']

    def set_conn_str(self, db, new_conn_str):

        self.dbs[db]['env_conn_str'] = new_conn_str


class TestConfig(Config):

    def __init__(self):

        super().set_conn_str('db_a',
                'postgresql+psycopg2://simon:postgres@localhost:5432/testing')
