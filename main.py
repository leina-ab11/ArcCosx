from helper_math_functions import is_nan, arccos_maclaurin, PI
from user_input import read_input

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