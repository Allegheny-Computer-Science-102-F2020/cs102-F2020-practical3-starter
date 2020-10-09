"""Test the functions that that compute the factorial values."""

from factorialmaker import factorial


def test_multiply_different_numbers():
    """Ensure that multiplying the list of integers works correctly."""
    values = [1, 2, 3, 4]
    multiplication_result = factorial.multiply(values)
    assert multiplication_result == 1 * 2 * 3 * 4


def test_multiply_different_numbers_reorder():
    """Ensure that multiplying the list of integers works correctly when reordered."""
    values = [4, 3, 2, 1]
    multiplication_result = factorial.multiply(values)
    assert multiplication_result == 1 * 2 * 3 * 4


def test_multiply_same_numbers_identity():
    """Ensure that multiplying the list of integers works correctly for identity."""
    values = [1, 1, 1, 1]
    multiplication_result = factorial.multiply(values)
    assert multiplication_result == 1


def test_multiply_same_numbers_contains_zero():
    """Ensure that multiplying the list of integers works correctly with zero."""
    values = [0, 1, 2, 3]
    multiplication_result = factorial.multiply(values)
    assert multiplication_result == 0


def test_multiply_same_numbers_contains_zero_reorder():
    """Ensure that multiplying the list of integers works correctly with zero and reordered."""
    values = [3, 2, 1, 0]
    multiplication_result = factorial.multiply(values)
    assert multiplication_result == 0


def test_factorial_1():
    """Ensure that 1! = 1 and the factorial list is correct."""
    # Reminder of the function's output:
    #   --> a tuple consisting of (n, n!)
    #       AND
    #   --> a list consisting of multiple tuples that looks like
    #       [(1, 1!), (2, 2!), (3, 3!), ..., (n, n!)]
    # these assertions are customized for the result of 1! = 1
    (factorial_result, factorial_list) = factorial.factorial_iterative(1)
    assert len(factorial_result) == 2
    assert factorial_result[0] == 1
    assert factorial_result[1] == 1
    assert len(factorial_list) == 1
    assert factorial_list[0] == (1, 1)


def test_factorial_3():
    """Ensure that 3! = 6 and the factorial list is correct."""
    # Reminder of the function's output:
    #   --> a tuple consisting of (n, n!)
    #       AND
    #   --> a list consisting of multiple tuples that looks like
    #       [(1, 1!), (2, 2!), (3, 3!), ..., (n, n!)]
    # these assertions are customized for the result of 3! = 6
    (factorial_result, factorial_list) = factorial.factorial_iterative(3)
    assert len(factorial_result) == 2
    assert factorial_result[0] == 3
    assert factorial_result[1] == 6
    assert len(factorial_list) == 3
    assert factorial_list == [(1, 1), (2, 2), (3, 6)]
