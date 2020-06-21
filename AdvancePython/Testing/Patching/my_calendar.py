import requests
from datetime import datetime


def is_weekday():
    today = datetime.today()
    return (0 <= today.weekday() < 5)


def get_holidays():
    r = requests.get('http://localhost.api.holidays')
    if r.status_code == 200: # success
        return r.json()
    return None
