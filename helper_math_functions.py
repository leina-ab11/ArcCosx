# This file contains math helper functions built from scratch.


# tolerance is 10^-6 to guarantee 3 decimal places of
# accuracy using Maclaurin's method.

TOL = 0.000001  
PI = 3.14159265358979 


def built_sqrt(x):
    """This method calculates the square root of a number x 
    without using the math library.
    """

    if x == 0:
        return f"{0:.1f}"

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
   return i != i

def arccos_maclaurin(x, tol=TOL):
    """Compute arccos(x) using the Maclaurin series for arcsin.
    Sums the series until the next term is < tol.
    """
    # set when x < 0
    flip = False    
    # answers exactly at the endpoints of the domain, there's no need to calculate the series
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
    # the index of the piece, starting from 0       
    n = 0   
    # the result of the series when computing the pieces
    result = 0.0

    while abs(piece) >= tol:
        piece = piece * (u**2 * (2*n + 1)**2) / ((2*n + 2) * (2*n + 3))
        total += piece
        n += 1

    # the result here is arcsin(u), multiplying by 2 to get arccos of |x| = 2*arcsin(u)
    result = 2 * total 
    # when x is negative we need to recover the sign of the result
    if flip:
        return PI - result
    
    return result