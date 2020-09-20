import os
import logging
from datetime import datetime

from dotenv import load_dotenv
from dateutil.parser import parse


load_dotenv()

LOG_FILE = os.getenv('LOG_FILE', None)
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = os.getenv('LOG_FORMAT', '%(name)s:%(funcName)s:%(levelname)s - %(message)s')

DATE_TIME_FORMAT = os.getenv('DATE_TIME_FORMAT', '%B %d, %Y %H:%M:%S')


def config_logger():
    logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)


def datetimeformat(value, format=DATE_TIME_FORMAT):
    if type(value) == str:
        return parse(value).strftime(format)

    return value.strftime(format)


def get_time_stamp():
    return datetime.now()
