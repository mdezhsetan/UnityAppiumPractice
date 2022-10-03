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


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        pytest.param("1+7", 8, marks=pytest.mark.basic),
        pytest.param("2+4", 6, marks=pytest.mark.basic, id="basic_2+4"),
        pytest.param(
            "6*9", 42, marks=[pytest.mark.basic, pytest.mark.xfail], id="basic_6*9"
        ),
    ],
)
def test_param_id(test_input, expected):
    assert eval(test_input) == expected
