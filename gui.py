import tkinter as tk
from helper_math_functions import arccos_maclaurin, is_nan, PI
from user_input import read_input



def calculate():
    user_input = entry.get().strip()
    try:
        i = read_input(user_input)
    except ValueError as err:
        result_label.config(text=f"Error: {err}")
        return
    result_in_rad = arccos_maclaurin(i)
    result_in_deg = result_in_rad * 180 / PI
    result_label.config(text=f"Rad: {result_in_rad:.3f}\nDegrees: {result_in_deg:.3f}")
    

root = tk.Tk()
root.title("D2: arccos(x) Calculator")
root.geometry("385x250")
root.resizable(False, False)

tk.Label(root, text="Enter x in [-1, 1]:").pack()
entry = tk.Entry(root)
entry.pack()
result_label = tk.Label(root, text="")      
result_label.pack()
tk.Button(root, text="Calculate", command=calculate).pack()

root.mainloop()