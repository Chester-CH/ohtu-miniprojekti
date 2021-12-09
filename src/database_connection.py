import sqlite3
import os

DATABASE_NAME = "reading_tips_database.db"
TEST_DATABASE_NAME = "test_database.db"


def create_database_connection(database_name=DATABASE_NAME):
    """Returns an sqlite3 database connection.
    """
    dirname = os.path.dirname(__file__)
    db_connection = sqlite3.connect(
        os.path.join(dirname, "..", "data", database_name))
    db_connection.row_factory = sqlite3.Row
    return db_connection


database_connection = create_database_connection()
