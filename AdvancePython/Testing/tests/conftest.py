import pytest
import smtplib

# If during implementing your tests you realize that you want to use a
# fixture function from multiple test files you can move it to a conftest.py file.
# You don’t need to import the fixture you want to use in a test,
# it automatically gets discovered by pytest.
# then test modules, then conftest.py files and finally builtin
# and third party plugins.

# scope = [function, class, module, package, session]
@pytest.fixture(scope='function')
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


# Fixture Finalization
# 'yield' statement instead of 'return'
@pytest.fixture(scope="module")
def smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection # release the fixture value
    print("teardown smtp")
    smtp_connection.close()
