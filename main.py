"""
Main file for the project. This is a Fire interface
which provides a commandline structure to the functions.
"""

import logging
import fire
from config import Config
from models import get_engine
from modules import log

LOGGER = logging.getLogger(__name__)


class Main():

    class CreateDb():

        def db_a(self):

            LOGGER.info('here')

            c = Config()

            e = get_engine(c.get_conn_str('db_a'))
            LOGGER.info(c.get_conn_str('db_a'))

            m = c.get_db_model('db_a')

            m.Base.metadata.create_all(e)


if __name__ == "__main__":
    """
    build the fire interface
    """
    fire.Fire(Main)
