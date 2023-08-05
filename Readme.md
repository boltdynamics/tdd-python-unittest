# Practical Test-Driven Development (TDD) with Python using the built-in unittest framework.

### Prerequisites

- Python 3
- pipenv (for managing Python environments)

Run `make check-prerequisites` to check if the prerequisites are installed.

### Initialize a pipenv python project

Run `make install-packages` to initialize the python project with dependencies. This will create a Pipfile and install the following python packages in the virtual environment:

- nose2 (for running unit tests)
- nose2-cov (for generating coverage reports)

### 3 rules of TDD

- ***RED*** -> write a test that fails.
- ***GREEN*** -> implement the test-supporting functionality to pass the test.
- ***REFACTOR*** -> improve the production code AND the tests to absolute perfection.

### Simple Calculator App

For the purpose of demonstrating TDD, we will develop a simple calculator app. The calculator app will have an `add()` function that takes two arguments and returns the sum of the arguments.

### Define requirements for calculator app

- The calculator should have a `add()` function that takes two arguments and returns the sum of the arguments.
- The `add()` function should return an integer.
- The `add()` function should validate the arguments and raise a `ValueError` if the arguments are not numbers.

### Starting development with TDD

1. Create a test file for the module you want to test. For example, if you want to test the `calculator.py` module, create a `test_calculator.py` file in `tests/` directory.
2. Write a test that fails. For example, if you want to test the `add()` function in `src/calculator.py`, write a test that calls `add()` with some arguments and assert that the result is what you expect. This is the ***RED*** step.
```python
from src.calculator import add

def test_add():
    result = add(1, 2)
    print(f"\n\nResult from add function --> {result}\n")
    assert result == 3
```

This will fail because the `add()` function is not implemented yet. Run `make test` to run the test.

3. Implement the test-supporting functionality to pass the test. For example, implement the `add()` function in `calculator.py` to return the sum of the arguments. This is the ***GREEN*** step.
```python
def add(a, b) -> int:
    return a + b
```

This will pass the test because the `add()` function now returns the sum of the arguments.

4. Improve the production code AND the tests to absolute perfection. For example, refactor the `add()` function to use the `sum()` function from the `operator` module. This is the ***REFACTOR*** step.
```python
def add(a, b) -> int:
    return sum([a, b])
```

5. Validate the arguments and raise a `ValueError` if the arguments are not numbers. For example, add a test that calls `add()` with non-numeric arguments and assert that a `ValueError` is raised. This is the ***RED*** step.
```python
from nose2.tools.such import helper

def test_add_raise_value_error_if_non_integers():
    with helper.assertRaises(ValueError):
        add("2", 5)
```

This will fail because the `add()` function does not validate the arguments.

6. Implement the test-supporting functionality to pass the test. For example, implement the `add()` function to validate the arguments and raise a `ValueError` if the arguments are not numbers. This is the ***GREEN*** step.
```python
def add(a, b) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Arguments must be integers.")
    return sum([a, b])
```

This will pass the test because the `add()` function now validates the arguments and raises a `ValueError` if the arguments are not numbers.

### Test coverage and reporting

Run `make test-with-coverage` to run the tests and generate a coverage report. The output will also show missing coverage lines in the source code.

The coverage report will be generated in `htmlcov/` directory. Open `htmlcov/index.html` in a browser or by using a VS Code extension to view the coverage report.

### Gotchas

Sometimes you want to test that a function calls another function. For example, you want to test that `some_other_function()` calls `function_that_does_some_calc()` with the correct arguments. You can use the `mocker` fixture to mock the `function_that_does_some_calc()` function and assert that it is called with the correct arguments.

```python
def function_that_does_some_calc(a, b):
        return a + b

def some_other_function(a, b):
    function_that_does_some_calc(a, b)
    return a * b
```

In this first test, when we test `some_other function()`, it calls the real `function_that_does_some_calc()` function as its not mocked. But the test coverage report will show that the `function_that_does_some_calc()` function has test coverage which is not true as we have not tested it.

```python
def test_some_other_function():
    result = some_other_function(2, 3)
    assert result == 6
```

To fix this, we can use the `patch` to mock the `function_that_does_some_calc()` function.

```python
from unittest.mock import patch

@patch("src.calculator.function_that_does_some_calc")
def test_some_other_function(mock_function_that_does_some_calc):
    result = some_other_function(2, 3)
    assert result == 6
```

Now the test coverage report will show that the `function_that_does_some_calc()` function has no test coverage which is true as we have mocked it.

Finally, we can test `function_that_does_some_calc()` function,

```python
def test_function_that_does_some_calc():
    result = function_that_does_some_calc(1, 2)
    assert result == 3
```
