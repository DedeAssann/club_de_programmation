"""
Module sa baw fonksyon pou kalkule suite fibonacci
"""


def fib(arg):
    """
    Write Fibonacci series up to arg.
    """
    a_value, b_value = 0, 1
    while a_value < arg:
        print(a_value, end=" ")
        a_value, b_value = b_value, a_value + b_value
    print()


def fib2(arg):
    """
    Return Fibonacci series up to arg
    """
    result = []
    a_value, b_value = 0, 1
    while a_value < arg:
        result.append(a_value)
        a_value, b_value = b_value, a_value + b_value
    return result


__all__ = ["fib", "fib2"]
