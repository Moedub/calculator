### calculator.py ###
import tkinter as tk
import math

def on_area_submit(entry: tk.Entry, shape: str, mode_label: tk.Label) -> None:
    """
    Calculate the area of a selected shape based on input dimensions.

    Args:
        entry: The entry widget where input is provided.
        shape: The shape type to calculate area for (e.g., "Circle").
        mode_label: Label widget indicating the current mode.
    """
    if "Area Calculation" not in mode_label.cget("text"):
        entry.delete(0, tk.END)
        entry.insert(0, "Error: Not in area mode")
        return

    try:
        values = list(map(float, entry.get().split()))  # Parse space-separated values
        if len(values) == 0:
            raise ValueError

        if shape == "Circle":
            result = math.pi * (values[0] ** 2)
        elif shape == "Rectangle" and len(values) == 2:
            result = values[0] * values[1]
        elif shape == "Triangle" and len(values) == 2:
            result = 0.5 * values[0] * values[1]
        elif shape == "Square":
            result = values[0] ** 2
        else:
            raise ValueError("Invalid input")

        entry.delete(0, tk.END)
        entry.insert(0, f"Area: {result:.2f}")
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
