def get_sqlite_db(path: str = '../database.db'):
    """get the sqlite db and open a connection with it.
    if the SQLite database does not exist. an error is thrown.

    Param: path {str} a path to the database

    Returns: connection to database 
    """
    return None


def create_sqlite_db(path: str = '../database.db', ingest: bool = False, ingest_path: str = '../temps.csv'):
    """create a new sqlite database with the correct schemas.
    This should be used when a SQLite database could not be found.
    This function can also optionally ingest data from a CSV file
    as a seed for the database.

    Param: path {str} a path to the database
    Param: ingest {bool} a boolean flag to check if ingest should be done
    Param: ingest_path {str} a path to the ingestible CSV file. 

    Returns: None
    """
    return None