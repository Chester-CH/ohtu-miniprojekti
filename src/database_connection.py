import sqlite3
import os

DATABASE_NAME = "reading_tips_database.db"
TEST_DATABASE_NAME = "test_database.db"

def create_database_connection(database_name=DATABASE_NAME):
    dirname = os.path.dirname(__file__)
    database_connection = sqlite3.connect(os.path.join(dirname, "..", "data", database_name))
    database_connection.row_factory = sqlite3.Row
    return database_connection

database_connection = create_database_connection()
