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


# yield syntax with `with`
# the connection will be autoclosed
@pytest.fixture(scope="module")
def smtp_connection():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
        yield smtp_connection


# addfinalizer for cleanup
# addfinalizer function comes from the 'request-context'
@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection


# instropect the 'requesting' function/class/module
# use the 'request.module' attribute to obtain 'smtpserver' attribute
@pytest.fixture(scope="function")
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print("finalizing {} ({})".format(smtp_connection, server))
    smtp_connection.close()
