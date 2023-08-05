def add(a, b) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print(f"\n\nArguments must be integers. Received {a} and {b}\n")
        raise ValueError("Arguments must be integers.")
    return sum([a, b])


def function_that_does_some_calc(a, b):
    return a + b


def some_other_function(a, b):
    function_that_does_some_calc(a, b)
    return a * b
