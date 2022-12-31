import sqlite3


def get_sqlite_db(db_path: str = '../database.db'):
    """get the sqlite db and open a connection with it.
    if the SQLite database does not exist, it is created along with tables

    Param: db_path {str} a path to the database

    Returns: connection to database 
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # create recordings table
    cursor.execute('''
              CREATE TABLE IF NOT EXISTS weather(
                recording_id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                temperature_hum REAL,
                temperature_pres REAL,
                humidity REAL,
                pressure REAL
              )
              ''')
    conn.commit()

    return conn


def load_data_into_db(db_path: str = '../database.db', csv_path: str = '../temps.csv'):
    """load csv data into a SQLite database

    Param: db_path {str} a path to the database file
    Param: csv_path {bool} a path to the csv file

    Returns: None
    """
    return None
