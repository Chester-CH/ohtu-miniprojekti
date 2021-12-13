from database_connection import database_connection as default_database_connection
# pylint: disable=missing-function-docstring


def create_tables(database_connection=default_database_connection):
    cursor = database_connection.cursor()
    sql = """CREATE TABLE Tips (
                id INTEGER PRIMARY KEY,
                type TEXT,
                title TEXT,
                datetime DATETIME,
                visible BOOLEAN,
                author TEXT,
                isbn TEXT,
                url TEXT,
                name TEXT,
                description TEXT
                );
          """

    cursor.execute(sql)
    database_connection.commit()


def drop_tables(database_connection=default_database_connection):
    cursor = database_connection.cursor()
    sql = "DROP TABLE IF EXISTS Tips;"
    cursor.execute(sql)
    database_connection.commit()


def initialize_database(database_connection=default_database_connection):
    drop_tables(database_connection)
    create_tables(database_connection)


if __name__ == "__main__":
    initialize_database()
