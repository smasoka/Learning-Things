import pytest


@pytest.fixture(params=['one', 'two', 'three'])
def parametrized_username(request):
    return request.param

@pytest.fixture
def non_parametrized_username(request):
    return 'username'
