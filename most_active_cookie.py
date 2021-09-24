import sys
from typing import Dict, List
from datetime import datetime
import csv
from collections import defaultdict


UTC_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
CLI_FORMAT = '%Y-%m-%d'

def process_cookie_log(cookie_log: str) -> dict[datetime, list[str]]:
    """
    Accepts path to cookie log and returns dictionary mapping date to list of active cookies
    """
    
    with open (cookie_log, 'r') as cookie_log:
        reader = csv.reader(cookie_log, delimiter=',')
        _ = next(reader)
        date_to_cookie = defaultdict(list)
        for line in reader:
            date_to_cookie[datetime.strptime(line[1], UTC_FORMAT).date()].append(line[0])
    return dict(date_to_cookie)


def get_most_active_cookies(log_date: str, date_to_cookie: dict) -> list[str]:
    """
    Accepts date provided in cli and returns list of most active cookies on input date
    """
    cookies_for_log_date = date_to_cookie[log_date]
    freq = defaultdict(lambda: 0)
    for cookie in cookies_for_log_date:
        freq[cookie]+=1
    most_active_count = max(freq.values())
    return [cookie for cookie in freq if freq[cookie] == most_active_count]

if __name__ == "__main__":
    ##to do: handle case when argv is not formatted properly, check for "-d"
    cookie_log = sys.argv[1]
    log_date = datetime.strptime(sys.argv[3], CLI_FORMAT).date()
    date_to_cookie = process_cookie_log(cookie_log)
    most_active_cookies = get_most_active_cookies(log_date, date_to_cookie)
    for each in most_active_cookies:
        sys.stdout.write(each + "\n")


    