import logging
import pathlib
from logging.handlers import RotatingFileHandler

# setup logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a rotating file handler for the logger
log_path = f"{pathlib.Path(__file__).parent.resolve()}/observer.log"
rotating_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=2)

# create a formatter for logs and add it to the rotating handler
formatter = logging.Formatter('%(asctime)s :: %(levelname)-8s :: %(message)s')
rotating_handler.setFormatter(formatter)

# add the rotating file handler to the logger
logger.addHandler(rotating_handler)