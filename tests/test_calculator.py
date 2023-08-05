from src.calculator import add
from nose2.tools.such import helper
from src.calculator import function_that_does_some_calc, some_other_function

from unittest.mock import patch


def test_add():
    result = add(5, 3)
    print(f"\n\nResult from add function --> {result}\n")
    assert result == 8


def test_add_raise_value_error_if_not_int():
    with helper.assertRaises(ValueError):
        add("cascsa", 9)


def test_some_other_function():
    result = some_other_function(2, 3)
    assert result == 6


@patch("src.calculator.function_that_does_some_calc")
def test_some_other_function(mock_function_that_does_some_calc):
    result = some_other_function(2, 3)
    assert result == 6


def test_function_that_does_some_calc():
    result = function_that_does_some_calc(1, 2)
    assert result == 3
