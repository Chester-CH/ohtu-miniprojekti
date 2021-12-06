from datetime import datetime
from entities.reading_tip import ReadingTip
from sqlite3.dbapi2 import DatabaseError
from database_connection import database_connection as default_database_connection

# pylint: disable=missing-function-docstring

def give_tip_object(row):
    return ReadingTip(row["id"], row["title"])

class TipsRepository:
    """Class for making SQL quaries dealing with reading tips.
    """

    def __init__(self, database_connection=default_database_connection):
        self._connection = database_connection

    def create_tip(self, title):
        try:
            sql = "INSERT INTO Tips (title, datetime, visible) \
                   VALUES (?, ?, TRUE);"
            time = datetime.now()
            cursor = self._connection.cursor()
            cursor.execute(sql, [title, time])
            self._connection.commit()
            return True
        except DatabaseError:
            return False

    def get_tips(self):
        sql = "SELECT * FROM Tips WHERE visible=TRUE;"
        cursor = self._connection.cursor()
        tips = cursor.execute(sql).fetchall()

        return list(map(give_tip_object, tips))

    def remove_tip(self, tip_id):
        try:
            sql = "UPDATE Tips SET visible=FALSE WHERE id=?;"
            cursor = self._connection.cursor()
            cursor.execute(sql, [tip_id])
            self._connection.commit()
            return True
        except DatabaseError:
            return False

tips_repository = TipsRepository()
