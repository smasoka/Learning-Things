def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    # assert b"mail.python.org" in msg
    # assert 0


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    # assert 0

# This value will be picked up by out fixture in 'conftest'
smtpserver = "mail.python.org"

def test_showhelo(smtp_connection):
    response, msg = smtp_connection.helo()
    assert response == 250
    assert b"mail.python.org" in msg
