import sqlite3
import os

dirname = os.path.dirname(__file__)
database_name = "reading_tips_database.db"
database_connection = sqlite3.connect(os.path.join(dirname, "..", "data", database_name))
database_connection.row_factory = sqlite3.Row