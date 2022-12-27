# standard lib

# third-party lib

# internal lib
from observer.logger import logger
from observer.database import create_sqlite_db, get_sqlite_db


def record_weather(db_conn):
    """Uses the sense hat board to record temperature, pressure, and humidity.

    Param: db_conn {connection} a connection to the SQLite db
    Returns: None
    """
    return None


if __name__ == "__main__":
    logger.info('🌅 Starting to collect weather...')
    try:
        logger.info('🗃️ database found')
        logger.info('🗃️ results written to database')
    except Exception as e:
        logger.error('💥 Something unexpected happened', stack_info=True)
