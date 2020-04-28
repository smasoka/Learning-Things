import math_func
import pytest
import sys

@pytest.mark.skip(reason = "do not run test_add")
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.skip(sys.version_info < (3,3), reason = "Python version not supported")
def test_product():
    assert math_func.product(5,5) == 25
    assert math_func.product(2) == 4
    assert math_func.product(7) == 14

@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Helow' not in result

@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result

def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36

# Using parametrize
@pytest.mark.parametrize('num1, num2, result',
    [
        (7, 3, 10),
        ('Hello ', 'World', 'Hello World'),
        (10.5, 25.5, 36)
    ]
)
def test_add_all(num1, num2, result):
    assert math_func.add(num1, num2) == result
