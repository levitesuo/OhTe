from database_connection import get_database_connection


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                   );
                   """)

    cursor.execute("""
                   CREATE TABLE grids (
                       grid_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       content TEXT NOT NULL,
                       owner_id INTEGER NOT NULL,
                       FOREIGN KEY (owner_id)
                            REFERENCES users (user_id)
                            ON DELETE CASCADE
                   );
                   """)
    connection.commit()


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
                   DROP TABLE users CASCADE;
                   """)
    cursor.execute("""
                   DROP TABLE grids CASCADE;
                   """)
    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
