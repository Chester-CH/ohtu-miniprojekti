from datetime import datetime
from sqlite3.dbapi2 import DatabaseError
from database_connection import database_connection as default_database_connection

# pylint: disable=missing-function-docstring

class TipsRepository:
    """Class for making SQL quaries dealing with reading tips.
    """

    def __init__(self, database_connection=default_database_connection):
        self._connection = database_connection

    def create_tip(self, title):
        try:
            sql = "INSERT INTO Tips (title, datetime) VALUES (?, ?);"
            time = datetime.now()
            cursor = self._connection.cursor()
            cursor.execute(sql, [title, time])
            self._connection.commit()
            return True
        except DatabaseError:
            return False

tips_repository = TipsRepository()
