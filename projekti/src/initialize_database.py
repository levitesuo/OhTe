from database_connection import get_database_connection, get_test_connection


def create_tables(connection):
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
                       grid_id TEXT,
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
    cursor = connection.cursor()
    cursor.execute("""
                   DROP TABLE IF EXISTS users;
                   """)
    cursor.execute("""
                   DROP TABLE IF EXISTS grids;
                   """)
    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


def initialize_test_database():

    connection = get_test_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
