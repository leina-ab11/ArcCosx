from helper_math_functions import is_nan


def read_input(userInput):
    """ Error handling for the user input when the user is out of the domain [-1,1]
    or when the user inputs non-numerical values.
    """
    try:
        x = float(userInput)
    except ValueError:
        raise ValueError(
            f"Syntax error: '{userInput}' is not a number. Enter a real number, e.g. 0.5."
        )
    if x < -1 or x > 1 or is_nan(x):
        raise ValueError(
            f"Domain error: arccos is undefined for x = {x}. Valid domain: [-1, 1]."
        )
    return x