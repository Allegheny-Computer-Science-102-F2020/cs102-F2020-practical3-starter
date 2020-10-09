"""Define the command-line interface for the iterator program."""

import typer

from factorialmaker import display
from factorialmaker import factorial


def main(
    # TODO: Add a typer option parameter for the --iterative command-line argument
    # TODO: Set the default value of this argument to be False
    # TODO: Add a typer option parameter for the "--number" command-line argument
    # TODO: set the min of this to be 1, the max to be 20, and the default to be 5
):
    """Compute sequence of factorial numbers with iteration or recursion."""
    # display the debugging output for the program's command-line arguments
    typer.echo("")
    typer.echo(
        f"Calculating {number}! and returning all numbers in the computation of {number}! 🛫"
    )
    typer.echo("")
    typer.echo(
        f"  Should I use an iterative function? {display.convert_bool_to_answer(iterative)}"
    )
    typer.echo("")
    # compute the sequence of factorial numbers and the value of number! using iteration
    if iterative is True:
        typer.echo("  Here is the output from the iterative function.")
        typer.echo("")
        # TODO: call the factorial.factorial_iterative function for the provided number
        # TODO: make sure to collect the tuple output that contains the computed
        # factorial ordered pair and the list of computed factorials in ordered pairs
        # TODO: refer to the test cases to learn more about the output format
        # TODO: make sure to reformat this function call using the Black code formatter
        # developed by the Python software foundation
        # use different approaches to display the result of the computation
        display.display_factorial_list(computed_factorials, "   ")
        display.display_factorial_unpack(computed_factorials, "   ")
        # TODO: Also display the computed factorial pair as the last output
        typer.echo("")
        # display a final message and some extra spacing
        typer.echo("Wow, computing factorial numbers is demanding! 😂")
        typer.echo("")


if __name__ == "__main__":
    typer.run(main)
