import pytest
import smtplib

@pytest.fixture(scope='function')
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

# If during implementing your tests you realize that you want to use a
# fixture function from multiple test files you can move it to a conftest.py file.
# You don’t need to import the fixture you want to use in a test,
# it automatically gets discovered by pytest.
# The discovery of fixture functions starts at test classes,
# then test modules, then conftest.py files and finally builtin
# and third party plugins.

# scope = [function, class, module, package, session]
