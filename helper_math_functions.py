"""Math helper functions built from scratch."""

# tolerance is 10^-6 to guarantee 3 decimal places of
# accuracy using Maclaurin's method.

TOL = 0.000001
PI = 3.14159265358979

# This is the maximum number of iterations to prevent
# infinite loops in case of convergence issues.
MAX_ITERATIONS = 100


class ConvergenceError(Exception):
    """Raised when the Maclaurin series
    does not converge within the iteration cap."""


def built_sqrt(x):
    """This method calculates the square root of a number x
    without using the math library.
    """

    if x == 0:
        return 0.0

    estimate = x
    while True:
        next_estimate = (estimate + x / estimate) / 2
        if abs(next_estimate - estimate) < TOL:
            return next_estimate
        estimate = next_estimate


def is_nan(i):
    """This method checks for not a number input.
    It replaces the math built in function.
    """
    return i != i       # pylint: disable=comparison-with-itself


def arccos_maclaurin(x, max_iterations=MAX_ITERATIONS):
    """Compute arccos(x) using the Maclaurin series for arcsin.
    Sums the series until the next term is < tol.
    """
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1]")
    # set when x < 0
    flip = False
    # answers exactly at the endpoints of the domain,
    # there's no need to calculate the series
    if x == 1:
        return 0.0
    if x == -1:
        return PI

    if x < 0:
        x = -x
        flip = True

    # we first need to reduce arccos(x) to arcsin(x)
    # to arccos(x) = 2*arcsin(u) where u = sqrt((1-x)/2)
    u = built_sqrt((1 - x) / 2)
    # the first piece of the series
    total = u
    # current piece, starts as term 0
    piece = u

    for n in range(max_iterations):
        piece = piece * (u**2 * (2*n + 1)**2) / ((2*n + 2) * (2*n + 3))
        total += piece
        if abs(piece) < TOL:
            result = 2 * total
            if flip:
                result = PI - result
            return result

    raise ConvergenceError(
        "Did not converge within the maximum number of iterations.")
