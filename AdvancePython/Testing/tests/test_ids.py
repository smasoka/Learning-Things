import pytest


# ids on each param
@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param
# this can be in conftest

def test_a(a):
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None


# ids based on a function
@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param
# this can be in conftest

def test_b(b):
    pass
