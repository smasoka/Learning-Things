import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

requests = Mock() # BING!

def get_holidays():
    r = requests.get('http://localhost.api.holidays')
    if r.status_code == 200: # success
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # mock the function that calls 'requests.get' to raise Timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()
