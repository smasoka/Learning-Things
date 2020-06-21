import unittest
from requests.exceptions import Timeout
from unittest.mock import patch

from my_calendar import requests, get_holidays

# patch as a decorator
class TestCalendar(unittest.TestCase):
    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


# patch as a context manager
class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch('my_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()


# patch an object's attrubutes instead of the whole object
class TestCalendar(unittest.TestCase):
    @patch.object(requests, 'get', side_effect=Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(Timeout):
            get_holidays()


if __name__ == '__main__':
    unittest.main()
