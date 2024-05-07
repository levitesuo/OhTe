from database_connection import get_database_connection, get_test_connection


def create_tables(connection):
    '''Creates the tables neccessary for the application to function.'''
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE users (
                        user_id TEXT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                   );
                   """)

    cursor.execute("""
                   CREATE TABLE grids (
                       grid_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       content TEXT NOT NULL,
                       owner_id INTEGER NOT NULL
                   );
                   """)
    connection.commit()
    cursor.execute("INSERT INTO users (username, password, user_id) VALUES (?, ?, ?)",
                   ("Guest", "Guest", "1"))
    connection.commit()


def drop_tables(connection):
    '''Drops the tables from the database.'''
    cursor = connection.cursor()
    cursor.execute("""
                   DROP TABLE IF EXISTS users;
                   """)
    cursor.execute("""
                   DROP TABLE IF EXISTS grids;
                   """)
    connection.commit()


def initialize_database():  # pragma: no cover
    '''
    Initializes the database by dropping the tables and creating them again.
    This function is ommited from coverage becouse we don't want to run tests on the actual database.
    '''

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


def initialize_test_database():
    '''
    Initializes the database by dropping the tables and creating them again.
    Test database is used for testing purposes.
    '''

    connection = get_test_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":  # pragma: no cover
    ''' Omited from coverage'''
    initialize_database()
