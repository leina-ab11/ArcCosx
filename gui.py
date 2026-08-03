import tkinter as tk
from helper_math_functions import arccos_maclaurin, is_nan, PI
from user_input import read_input



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
    result_in_deg = result_in_rad * 180 / PI
    result_label.config(text=f"Rad: {result_in_rad:.3f}\nDegrees: {result_in_deg:.3f}")
    
def clear_input():
    """Clears the entry and result label."""
    entry.delete(0, tk.END)
    result_label.config(text="")

def exit_app():
    """Exits the application."""
    root.destroy()

root = tk.Tk()
root.title("D2: arccos(x) Calculator")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter x in [-1, 1] to calculate arccos(x):").pack(anchor="center", pady=(12, 6))
entry = tk.Entry(root, width=25)
entry.pack(anchor="center", pady=6)
result_label = tk.Label(root, text="")
result_label.pack(anchor="center", pady=6)
button_frame = tk.Frame(root)
button_frame.pack(anchor="center", pady=(6, 12))

tk.Button(button_frame, text="Calculate", command=calculate).pack(side="left", padx=6)
tk.Button(button_frame, text="Clear Input", command=clear_input).pack(side="left", padx=6)
tk.Button(button_frame, text="Exit", command=exit_app).pack(side="left", padx=6)

root.mainloop()