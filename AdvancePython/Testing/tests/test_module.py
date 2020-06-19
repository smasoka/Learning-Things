import pytest


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg", param)
    yield param
    print("  TEARDOWN modarg", param)


@pytest.fixture(scope="function", params=[1,2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg", param)
    yield param
    print("  TEARDOWN otherarg", param)


def test_0(otherarg):
    print("RUN test_0 with otherarg", otherarg)


def test_1(modarg):
    print("RUN test_1 with modarg", modarg)


def test_2(otherarg, modarg):
    print("RUN test_2 with otherarg {} and modarg {}".format(otherarg, modarg))


# Play around with the scope and see how pytest works its magic 
