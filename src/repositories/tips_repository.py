from datetime import datetime
from entities.reading_tip import ReadingTip
from sqlite3.dbapi2 import DatabaseError
from database_connection import database_connection as default_database_connection

# pylint: disable=missing-function-docstring

def give_tip_object(row):
    return ReadingTip(row["title"])

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

    def get_tips(self):
        sql = "SELECT * FROM Tips;"
        cursor = self._connection.cursor()
        tips = cursor.execute(sql).fetchall()

        return list(map(give_tip_object, tips))

tips_repository = TipsRepository()
