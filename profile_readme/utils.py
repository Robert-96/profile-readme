import os
import logging
from datetime import datetime

from dotenv import load_dotenv
from dateutil.parser import parse


load_dotenv()

LOG_FILE = os.getenv('LOG_FILE', None)
LOG_LEVEL = os.getenv('LOG_LEVEL', 'CRITICAL')
LOG_FORMAT = os.getenv('LOG_FORMAT', '%(name)s:%(funcName)s:%(levelname)s - %(message)s')

DATE_TIME_FORMAT = os.getenv('DATE_TIME_FORMAT', '%B %d, %Y %H:%M:%S')


def config_logger():
    """Does basic configuration for the logging system."""

    logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)


def datetimeformat(value, format=DATE_TIME_FORMAT):
    """Return a string representing the date, controlled by an explicit format string."""

    if type(value) == str:
        return parse(value).strftime(format)

    return value.strftime(format)


def get_time_stamp():
    """Return the current local date and time."""

    return datetime.now()
