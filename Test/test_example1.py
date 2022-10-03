import pytest


@pytest.fixture()
def number():
    return 20


def func(x):
    return x + 1


@pytest.mark.one
def test_method2(number):
    assert number != 6


# We have to use the exact x,y,z parameters as the next method's arguments
@pytest.mark.parametrize("x,y,z", [(1, 2, 3), (2, 3, 4), (4, 6, 10)])
def test_param(x, y, z):
    assert x + y == z
