"""GUI for the arccos(x) calculator."""
__version__ = "1.3.0"
import tkinter as tk
from helper_math_functions import arccos_maclaurin, PI
from user_input import read_input


def to_degrees(radians):
    """Convert radians to degrees (FR-4)."""
    return radians * 180 / PI


def format_result(radians, degrees):
    """Format the arccos result to 3 decimal places (FR-5)."""
    return f"Rad: {radians:.3f}\nDegrees: {degrees:.3f}"


def calculate():
    """
    Calculates the arccos of the input value and updates the result label.
    """
    user_input = entry.get().strip()
    try:
        i = read_input(user_input)
    except ValueError as err:
        result_label.config(text=f"Error: {err}")
        return
    result_in_rad = arccos_maclaurin(i)
    result_in_deg = to_degrees(result_in_rad)
    result_label.config(text=format_result(result_in_rad, result_in_deg))


def clear_input():
    """Clears the entry and result label."""
    entry.delete(0, tk.END)
    result_label.config(text="")


def exit_app():
    """Exits the application."""
    root.destroy()


def main():
    """Build and launch the calculator window."""
    global root, entry, result_label        # pylint: disable=global-variable-undefined
    root = tk.Tk()
    root.title("D2: arccos(x) Calculator - Version " + __version__)
    root.geometry("400x250")
    root.resizable(False, False)

    tk.Label(root, text="Enter x in [-1, 1] to calculate arccos(x):").pack(
        anchor="center", pady=(12, 6))
    entry = tk.Entry(root, width=25)
    entry.pack(anchor="center", pady=6)
    result_label = tk.Label(root, text="")
    result_label.pack(anchor="center", pady=6)
    button_frame = tk.Frame(root)
    button_frame.pack(anchor="center", pady=(6, 12))

    tk.Button(button_frame, text="Calculate",
              command=calculate).pack(side="left", padx=6)
    tk.Button(button_frame, text="Clear Input",
              command=clear_input).pack(side="left", padx=6)
    tk.Button(button_frame, text="Exit", command=exit_app).pack(
        side="left", padx=6)

    root.mainloop()


if __name__ == "__main__":
    main()
