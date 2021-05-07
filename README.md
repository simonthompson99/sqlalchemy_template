# README

This is supposed to be somewhat of a template for a project that uses SQLAlchemy to connect to a variety of different databases. I was trying to put together a generic structure for:

* sourcing local config details from a `.env` file;
* an extensible way to add new models for different databases and creating a single session object with all associated engines;
* a structure for adding unit tests;
* creating terminal and file logging

The `.env` file is not in the repo, one should be created for each environment e.g.:

`
DB_A_CONN_STR=postgresql+psycopg2://simon:password@localhost:5432/postgres
`

To run the unit tests, activate the virtual environment and run `python -m unittest`
