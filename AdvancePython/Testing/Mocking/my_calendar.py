# from datetime import datetime


# def is_weekday():
#     today = datetime.today()
#     print(today.weekday())
#     return (0 <= today.weekday() < 5)
#
# assert not is_weekday()

# this passes or fails depending on the day you run the test.
# This means the test results are not reliable and are not predictible
# So we need to Mock a few things

import datetime
from unittest.mock import Mock

tuesday = datetime.datetime(year=2020, month=6, day=2)
saturday = datetime.datetime(year=2020, month=6, day=6)

datetime = Mock() #BING!


def is_weekday():
    today = datetime.datetime.today()
    return (0 <= today.weekday() < 5)

# define a return value for .today() to the tuesday
datetime.datetime.today.return_value = tuesday
assert is_weekday()

# define a return value for S.today() to be saturday
datetime.datetime.today.return_value = saturday
assert not is_weekday()
