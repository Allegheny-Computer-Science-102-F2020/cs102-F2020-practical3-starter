"""Print values and lists of values."""

from typing import List
from typing import Tuple


def convert_bool_to_answer(argument: bool) -> str:
    """Return a string-based and human-readable representation of a bool."""
    if argument:
        return "Yes"
    return "No"


def display_factorial_list(values: List, indent=""):
    """Display the entire list of all the computed factorial values."""
    total_values = len(values)
    print(f"{indent}Factorial values for {total_values}! = {values}")


def display_factorial_unpack(values: List, indent=""):
    """Display the final computed factorial value, namely n!."""
    total_values = len(values)
    print(
        f"{indent}Unpacking at end of list to determine {total_values}! = {values[-1][1]}"
    )


def display_factorial_pair(factorial_number_pair: Tuple[int, int], indent=""):
    """Display the specific computed factorial number."""
    print(
        f"{indent}The returned ordered pair shows that {factorial_number_pair[0]}! = {factorial_number_pair[1]}"
    )
