"""
folder holds the various different sqlalchemy models for the project
session connected to the various required engines created here
"""

import importlib
import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

LOGGER = logging.getLogger(__name__)


def assemble_binds(config):
    """
    assemble binds for the different models
    :param config: an instance of the Config class
    :returns: dictionary that can be passed to session.configure
    """

    binds = {}

    for db in config.dbs.keys():

        m = config.get_db_model(db)

        # add the engine to the dictionary of binds
        binds[m.Base] = get_engine(config, db)

    return binds


def make_session(config):
    """
    get SQLAlchemy session bound to all required DBs
    :param config: an instance of the Config class
    :returns: session bound to all databases in config.dbs
    """

    LOGGER.debug("making session")

    session = sessionmaker(autoflush=False)
    session.configure(
        binds=assemble_binds(config)
    )

    return session()


def get_engine(config, db):
    """
    Get an engine for a db
    :param conn_str: psycopg2 connection string for db
    """

    LOGGER.debug(f"received call to get_engine for {db}")

    return create_engine(config.get_conn_str(db), echo=True)


def create_database(config, db):
    """
    creates the tables for a given database
    :param config: instance of Config class
    :param db: the database to be created
    """

    LOGGER.debug(f"received call to create {db} database")

    e = get_engine(config, db)

    m = config.get_db_model(db)

    m.Base.metadata.create_all(e)

def drop_database(config, db):
    """
    drops all the tables for a given database
    :param config: instance of Config class
    :param db: the database to be dropped
    """

    LOGGER.debug(f"received call to drop {db} tables")

    m = config.get_db_model(db)

    e = get_engine(config, db)

    m.Base.metadata.drop_all(e)



