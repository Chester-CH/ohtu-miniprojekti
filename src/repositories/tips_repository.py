from datetime import datetime
from sqlite3.dbapi2 import DatabaseError
from database_connection import database_connection as default_database_connection
from services.reading_tip_factory import ReadingTipFactory
# pylint: disable=missing-function-docstring


def give_tip_object(row):
    """A helper function for creating tip objects from row objects."""
    row_dict = dict(row)
    row_dict["tip_id"] = row["id"]
    tip = ReadingTipFactory.get_new_reading_tip(row_dict["type"])
    tip.set_values_from_dict(row_dict)
    return tip


class TipsRepository:
    """Class for making SQL quaries dealing with reading tips.
    """

    def __init__(self, database_connection=default_database_connection):
        self._connection = database_connection

    def get_tips(self):
        sql = "SELECT * FROM Tips WHERE visible=TRUE;"
        cursor = self._connection.cursor()
        tips = cursor.execute(sql).fetchall()

        return list(map(give_tip_object, tips))

    def remove_tip(self, tip_id):
        try:
            sql = "UPDATE Tips SET visible=FALSE WHERE id=? AND visible=TRUE;"
            cursor = self._connection.cursor()
            cursor.execute(sql, [tip_id])
            self._connection.commit()

            if cursor.rowcount == 1:
                return True
            return False
        except DatabaseError:
            return False

    def store_reading_tip(self, tip):

        def add_content(contents, key):
            if key not in contents.keys():
                return None
            return contents[key]


        try:
            cursor = self._connection.cursor()
            contents = tip.get_contents()
            if not tip["tip_id"]:
                sql = """INSERT INTO Tips (type, title, visible, author, isbn,
                         url, name, description, datetime)
                         VALUES (?, ?, TRUE, ?, ?, ?, ?, ?, ?)"""
                cursor.execute(
                    sql, [
                        add_content(contents, "tip_type"),
                        add_content(contents, "title"),
                        add_content(contents, "author"),
                        add_content(contents, "isbn"),
                        add_content(contents, "url"),
                        add_content(contents, "name"),
                        add_content(contents, "description"),
                        datetime.now()
                    ]
                )
                self._connection.commit()
                tip["tip_id"] = cursor.lastrowid
                return True

            # Update old data
            sql = """UPDATE Tips SET title=?, author=?,
                     isbn=?, url=?, name=?, description=?
                     WHERE id=? AND visible=TRUE"""

            cursor.execute(
                sql, [
                    add_content(contents, "title"),
                    add_content(contents, "author"),
                    add_content(contents, "isbn"),
                    add_content(contents, "url"),
                    add_content(contents, "name"),
                    add_content(contents, "description"),
                    add_content(contents, "tip_id")
                ]
            )
            self._connection.commit()
            if cursor.rowcount == 1:
                return True
            return False
        except DatabaseError:
            return False

tips_repository = TipsRepository()
