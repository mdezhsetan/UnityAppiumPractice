import pytest


@pytest.fixture()
def number():
    return 20


def func(x):
    return x + 1


def test_method2(number):
    assert number != 6
