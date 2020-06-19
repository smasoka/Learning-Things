import pytest

@pytest.fixture
def smtp_connection():
    import smtplib

    return smtplib.SMTP('smtp.gmail.com', 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0

# pytest finds 'test_ehlo' function because of prefix 'test_'
# 'test_ehlo' requires arg 'smtp_connection'
# so pytest looks for a function marked by 'fixure' called 'smtp_connection'
# smtp_connection() is called to create an instance
# test_ehlo(<smtp_connection instance>) is called
# fails at last line 'assert 0'
