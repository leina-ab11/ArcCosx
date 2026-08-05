"""GUI for the arccos(x) calculator."""
__version__ = "1.4.0"
import tkinter as tk
from tkinter import ttk
from helper_math_functions import arccos_maclaurin, PI
from user_input import read_input

# Colour palette
BG = "#1e2230"
CARD_BG = "#282c3e"
ACCENT = "#7c9dff"
ACCENT_DARK = "#5f7fe0"
TEXT_PRIMARY = "#eef0f7"
TEXT_MUTED = "#c2c8dc"
SUCCESS = "#7ee0a6"
ERROR = "#ff8a8a"
ENTRY_BG = "#333850"


def to_degrees(radians):
    """Convert radians to degrees (FR-4)."""
    return radians * 180 / PI


def format_result(radians, degrees):
    """Format the arccos result to 3 decimal places (FR-5)."""
    return f"Rad: {radians:.3f}\nDegrees: {degrees:.3f}"


def calculate():
    """Calculates the arccos of the input value and updates the result label."""
    user_input = entry.get().strip()
    try:
        i = read_input(user_input)
        result_in_rad = arccos_maclaurin(i)
        result_in_deg = to_degrees(result_in_rad)
        result_label.config(
            text="Result: \n" + format_result(result_in_rad, result_in_deg),
            foreground=SUCCESS)
    except ValueError as err:
        result_label.config(text=f"Error: {err}", foreground=ERROR)


def clear_input():
    """Clears the entry and result label."""
    entry.delete(0, tk.END)
    result_label.config(text="")
    entry.focus_set()


def exit_app():
    """Exits the application."""
    root.destroy()


def _build_style():
    """Configure the ttk style used across the window."""
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Card.TFrame", background=CARD_BG)
    style.configure("Root.TFrame", background=BG)

    style.configure("Title.TLabel", background=CARD_BG, foreground=TEXT_PRIMARY,
                    font=("Segoe UI", 16, "bold"))
    style.configure("Subtitle.TLabel", background=CARD_BG, foreground=TEXT_MUTED,
                    font=("Segoe UI", 12))
    style.configure("Result.TLabel", background=CARD_BG, foreground=TEXT_PRIMARY,
                    font=("Consolas", 12), justify="center", wraplength=520)

    style.configure("TEntry", fieldbackground=ENTRY_BG, foreground=TEXT_PRIMARY,
                    bordercolor=ACCENT, insertcolor=TEXT_PRIMARY,
                    borderwidth=1, relief="flat", padding=8)
    style.map("TEntry", bordercolor=[("focus", ACCENT)])

    style.configure("Accent.TButton", background=ACCENT, foreground="#1a1a1a",
                    font=("Segoe UI", 10, "bold"), borderwidth=0, padding=(14, 8))
    style.map("Accent.TButton", background=[("active", ACCENT_DARK)])

    style.configure("Ghost.TButton", background=CARD_BG, foreground=TEXT_PRIMARY,
                    font=("Segoe UI", 10), borderwidth=1, padding=(14, 8))
    style.map("Ghost.TButton", background=[("active", ENTRY_BG)])

    style.configure("Exit.TButton", background=CARD_BG, foreground=ERROR,
                    font=("Segoe UI", 10), borderwidth=1, padding=(14, 8))
    style.map("Exit.TButton", background=[("active", ENTRY_BG)])

    return style


def main():
    """Build and launch the calculator window."""
    global root, entry, result_label        # pylint: disable=global-variable-undefined
    root = tk.Tk()
    root.title("arccos(x) Calculator - Version " + __version__)
    root.geometry("650x380")
    root.resizable(False, False)
    root.configure(background=BG)

    _build_style()

    root.eval("tk::PlaceWindow . center")

    outer = ttk.Frame(root, style="Root.TFrame", padding=20)
    outer.pack(fill="both", expand=True)

    card = ttk.Frame(outer, style="Card.TFrame", padding=24)
    card.pack(fill="both", expand=True)

    ttk.Label(card, text="arccos(x) Calculator",
              style="Title.TLabel").pack(anchor="center", pady=(0, 4))
    ttk.Label(card, text="Enter x in [-1, 1] to calculate arccos(x)",
              style="Subtitle.TLabel").pack(anchor="center", pady=(0, 16))

    entry = ttk.Entry(card, width=20, justify="center",
                      font=("Segoe UI", 12))
    entry.pack(anchor="center", pady=(0, 16), ipady=4)
    entry.focus_set()
    entry.bind("<Return>", lambda _event: calculate())

    result_label = ttk.Label(card, text="", style="Result.TLabel")
    result_label.pack(anchor="center", pady=(0, 20))

    button_frame = ttk.Frame(card, style="Card.TFrame")
    button_frame.pack(anchor="center")

    ttk.Button(button_frame, text="Calculate", style="Accent.TButton",
               command=calculate).pack(side="left", padx=6)
    ttk.Button(button_frame, text="Clear", style="Ghost.TButton",
               command=clear_input).pack(side="left", padx=6)
    ttk.Button(button_frame, text="Exit", style="Exit.TButton",
               command=exit_app).pack(side="left", padx=6)

    root.mainloop()


if __name__ == "__main__":
    main()
