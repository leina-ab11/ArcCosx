"""User input handling for the arccos(x) calculator."""
from helper_math_functions import is_nan


def read_input(user_input):
    """ Error handling for the user input when the user is out of the domain [-1,1]
    or when the user inputs non-numerical values.
    """
    try:
        x = float(user_input)
    except ValueError as exc:
        raise ValueError(
            f"Syntax error: '{user_input}' is not a number. Enter a real number, e.g. 0.5."
        ) from exc
    if x < -1 or x > 1 or is_nan(x):
        raise ValueError(
           f"Domain error: arccos is undefined for x = {x}. Valid domain: [-1, 1]."
        )
    return x
