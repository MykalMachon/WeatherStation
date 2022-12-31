# standard lib
from pathlib import Path

# internal lib
from observer.logger import logger
from observer.services.database import get_sqlite_db
from observer.services.sensors import get_sensor_data


if __name__ == "__main__":
    logger.info('🌅 Starting to collect weather...')
    try:
        db_path = f"{Path(__file__).parent.resolve().parent.resolve()}/weather.db"

        conn = get_sqlite_db(db_path=db_path)
        logger.info('🗃️ database found and connected')

        weather = get_sensor_data()
        logger.info('🌡️ Weather has been recorded from sensors')

        cursor = conn.cursor()
        cursor.execute(f'''
                       INSERT INTO weather (temperature_hum, temperature_pres, humidity, pressure)
                       VALUES ({weather.get('t_hum')}, {weather.get('t_pres')}, {weather.get('hum')}, {weather.get('pres')})
                       ''')
        conn.commit()

        logger.info('🗃️ results written to database')
        logger.info('😴 shutting down...')
    except Exception as e:
        logger.error('💥 Something unexpected happened', stack_info=True)
