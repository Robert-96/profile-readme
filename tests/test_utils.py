import unittest.mock as mock
from datetime import datetime

from profile_readme.utils import datetimeformat, get_time_stamp

import pytest


@mock.patch('profile_readme.utils.datetime')
def test_get_time_stamp(datetime_mock):
    date = datetime(2020, 8, 24, 0, 0, 0, 0)

    datetime_mock.now = mock.Mock()
    datetime_mock.now.return_value = date

    assert get_time_stamp() == date


@pytest.mark.parametrize(
    "date, expected",
    [
        (datetime(2020, 8, 24, 0, 0, 0, 0), 'August 24, 2020 00:00:00'),
        (datetime(2020, 8, 24, 0, 0, 0, 0).strftime('%Y-%m-%d, %H:%M:%S'), 'August 24, 2020 00:00:00')
    ]
)
def test_datetimeformat(date, expected):
    assert datetimeformat(date) == expected
