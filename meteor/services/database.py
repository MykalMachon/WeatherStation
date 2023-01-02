import sqlite3

def get_sqlite_db(db_path: str = '../database.db') -> sqlite3.Connection:
    """get the sqlite db and open a connection with it.
    if the SQLite database does not exist, it is created along with tables

    Param: db_path {str} a path to the database

    Returns: connection to database 
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn