#!/usr/bin/env python3
from most_active_cookie import process_cookie_log, get_most_active_cookies, UTC_FORMAT, CLI_FORMAT
import csv
import datetime

def test_process_cookie_log() -> None:
    """
    Testing whether the process_cookie_log function works correctly.
    """
    cookie_log = 'test_logs/test_log_1.csv'
    date_to_cookie = process_cookie_log(cookie_log)
    assert date_to_cookie == {datetime.date(2018, 12, 9):['AtY0laUfhglK3lC7'], datetime.date(2018, 12, 8):['fbcn5UAVanZf6UtG'], datetime.date(2018, 12, 7):['4sMM2LxV07bPJzwf']}   

def test_get_most_active_cookies() -> None:
    """
    Testing whether the get_most_active_cookies function works correctly.
    """
    cookie_log = 'test_logs/test_log_1.csv'
    date_to_cookie = process_cookie_log(cookie_log)
    log_date = datetime.datetime.strptime('2018-12-08', CLI_FORMAT).date()
    most_active_cookies = get_most_active_cookies(log_date, date_to_cookie)
    assert sorted(most_active_cookies) == sorted(['fbcn5UAVanZf6UtG'])
if __name__ == "__main__":
    import pytest
    pytest.main(['most_active_cookie_test.py'])
