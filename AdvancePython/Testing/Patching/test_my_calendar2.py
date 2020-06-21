from unittest.mock import patch

import my_calendar

with patch('my_calendar.is_weekday', autospec=True):
    print(my_calendar.is_weekday())

# scope matters
from my_calendar import is_weekday

with patch('my_calendar.is_weekday', autospec=True):
    print(is_weekday()) # prints the actual function. Hierachy!

# to correct this
with patch('__main__.is_weekday', autospec=True):
    print(is_weekday())
