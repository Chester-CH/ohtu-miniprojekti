from datetime import datetime
from database_connection import database_connection as default_database_connection

class TipsRepository:
    def __init__(self, database_connection=default_database_connection):
        self._connection = database_connection

    def create_tip(self, title):
        try:
            sql = "INSERT INTO Tips (title, datetime) VALUES (?, ?);"
            time = datetime()
            cursor = self._connection.cursor()
            cursor.execute(sql, [title, time])
            self._connection.commit()
            return True
        except:
            return False

tips_repository = TipsRepository()
