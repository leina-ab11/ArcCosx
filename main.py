import math

# tolerance is 10^-6 to guarantee 3 decimal places of
# accuracy using Maclaurin's method.

TOL = 0.000001  
PI = 3.14159265358979 

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
    u = math.sqrt((1 - x) / 2)
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
    if x < -1 or x > 1 or math.isnan(x):
        raise ValueError(
            f"Domain error: arccos is undefined for x = {x}. Valid domain: [-1, 1]."
        )
    return x


def main():
    """Textual user interface for the user to use 
    and it prompts the user to enter a value or q to quit the system. 
    """
    print("++++ arccos(x) Calculator (F1) ++++")
    print("Computes the inverse cosine of x, for x in [-1, 1].")
    print("++++++++++++++++++++++++++++++++++++\n")
    print("Enter a value for x, or 'q' to quit.\n")

    # keep looping until user quits 
    while True:  
        userInput = input("arccos(x): enter x in [-1, 1]: ").strip()

        if "q" == userInput.lower():  
            print("Goodbye!")
            break

        try:
            x = read_input(userInput)
        except ValueError as err:
            print(f"  {err}\n")  
            continue

        result_rad = arccos_maclaurin(x)
        result_deg = result_rad * 180 / PI

        if result_deg == 0.000 and result_rad == 0.000:
            print(f"  arccos({x}) = 0 rad = 0 deg\n")
        else:
            print(f"  arccos({x}) = {result_rad:.3f} rad = {result_deg:.3f} deg\n")


if __name__ == "__main__":
    main()