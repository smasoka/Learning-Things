import pytest


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param
# this can be in conftest


def test_data_set(data_set):
    pass
