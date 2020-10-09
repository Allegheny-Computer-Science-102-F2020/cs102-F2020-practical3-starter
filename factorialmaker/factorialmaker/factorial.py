"""Compute the value of n! and all factorial values in the sequence leading up to n!."""

# TODO: import the List and Tuple type annotations
# that are used in the signatures of the functions


def multiply(values: List[int]) -> int:
    """Multiple together all of the values in the list."""
    # TODO: Use a for loop to multiply together all of the numbers in the list
    # TODO: Return the computed integer value


def factorial_iterative(number: int) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
    """Use iteration to calculate the value of n! and all factorial values up to n."""
    # create an empty list to store the ordered pairs of (n, n!)
    factorial_list = []
    # use this variable value to designate n
    value = 1
    # use this variable factorial_value to designate n!
    factorial_value = 1
    # TODO: iterate through the numbers in the range of 1 up to and including number
    for value in values:
        # TODO: compute the factorial for the current value
        # this means that we are calculating value!
        # TODO: store the ordered pair of (value, and factorial_value)
        # inside of the factor list for later return
    # TODO: return a tuple that contains:
    #   --> a tuple consisting of (n, n!)
    #       AND
    #   --> a list consisting of multiple tuples that looks like
    #       [(1, 1!), (2, 2!), (3, 3!), ..., (n, n!)]
