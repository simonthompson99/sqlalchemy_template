"""
Main file for the project. This is a Fire interface
which provides a commandline structure to the functions.
"""

import logging
import fire
from config import Config
from models import create_database
from modules import log

LOGGER = logging.getLogger(__name__)


class Main():

    class CreateDb():

        def db_a(self):

            LOGGER.info('creating db_a')

            c = Config()

            create_database(c, 'db_a')


if __name__ == "__main__":
    """
    build the fire interface
    """
    fire.Fire(Main)
