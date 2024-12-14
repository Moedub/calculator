import tkinter as tk
from tkinter import ttk
from area_logic import AreaLogic
from calculator_logic import CalculatorLogic


class CalculatorApp:
    """
    A Tkinter-based calculator app with standard and area calculation modes.
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Initializes the calculator application.
        """
        self.root = root
        self.root.title("Calculator Project")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.mode = "standard"  # Default mode is 'standard'
        self.create_standard_calculator()

    def create_standard_calculator(self) -> None:
        """
        Creates the standard calculator UI.
        """
        self.clear_gui()
        self.display = tk.StringVar()

        display_entry = ttk.Entry(self.root, textvariable=self.display, font=("Arial", 18), justify="right")
        display_entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('Clear', 5, 0), ('Delete', 5, 1), ('Mode', 5, 2)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                action = self.evaluate_expression
            elif text == 'Mode':
                action = self.switch_mode
            elif text == 'Clear':
                action = self.clear_display
            elif text == 'Delete':
                action = self.delete_last_character
            else:
                action = lambda t=text: self.add_to_display(t)

            ttk.Button(self.root, text=text, command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def create_area_calculator(self) -> None:
        """
        Creates the area calculator UI.
        """
        self.clear_gui()

        # Shape selection
        self.shape_selection = tk.StringVar(value="Circle")
        shapes = ["Circle", "Rectangle", "Triangle", "Square"]
        for i, shape in enumerate(shapes):
            ttk.Radiobutton(self.root, text=shape, variable=self.shape_selection, value=shape).grid(row=0, column=i, padx=5, pady=5)

        # Input fields
        ttk.Label(self.root, text="Base / Radius:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.base_radius_entry = ttk.Entry(self.root)
        self.base_radius_entry.grid(row=1, column=1, columnspan=3, sticky="ew", padx=5, pady=5)

        ttk.Label(self.root, text="Height:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.height_entry = ttk.Entry(self.root)
        self.height_entry.grid(row=2, column=1, columnspan=3, sticky="ew", padx=5, pady=5)

        # Buttons
        ttk.Button(self.root, text="Submit", command=self.calculate_area).grid(row=3, column=1, pady=10)
        ttk.Button(self.root, text="Clear", command=self.clear_display).grid(row=3, column=2, pady=10)
        ttk.Button(self.root, text="Mode", command=self.switch_mode).grid(row=4, column=1, columnspan=2)

        # Result display
        ttk.Label(self.root, text="Area:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=5, column=1, columnspan=3, sticky="ew", padx=5, pady=5)

    def add_to_display(self, value: str) -> None:
        """
        Adds a value to the calculator's display.
        """
        self.display.set(self.display.get() + value)

    def evaluate_expression(self) -> None:
        """
        Evaluates the mathematical expression in the display.
        """
        try:
            result = eval(self.display.get())
            self.display.set(str(result))
        except Exception:
            self.display.set("Error")

    def delete_last_character(self) -> None:
        """
        Deletes the last character from the calculator's display.
        """
        current_text = self.display.get()
        if current_text:
            self.display.set(current_text[:-1])

    def calculate_area(self) -> None:
        """
        Calculates the area based on the selected shape and inputs.
        """
        try:
            shape = self.shape_selection.get()
            base_radius = float(self.base_radius_entry.get())
            height = float(self.height_entry.get()) if self.height_entry.get() else 0

            if shape == "Circle":
                result = AreaLogic.calculate_circle_area(base_radius)
            elif shape == "Rectangle":
                result = AreaLogic.calculate_rectangle_area(base_radius, height)
            elif shape == "Triangle":
                result = AreaLogic.calculate_triangle_area(base_radius, height)
            elif shape == "Square":
                result = AreaLogic.calculate_square_area(base_radius)
            else:
                result = "Invalid shape"

            self.result_label.config(text=f"Area = {result:.2f}")
        except ValueError:
            self.result_label.config(text="Invalid input")

    def clear_display(self) -> None:
        """
        Clears the display and input fields.
        """
        if self.mode == "standard":
            self.display.set("")
        else:
            self.base_radius_entry.delete(0, tk.END)
            self.height_entry.delete(0, tk.END)
            self.result_label.config(text="")

    def switch_mode(self) -> None:
        """
        Switches between standard and area calculator modes.
        """
        if self.mode == "standard":
            self.mode = "area"
            self.create_area_calculator()
        else:
            self.mode = "standard"
            self.create_standard_calculator()

    def clear_gui(self) -> None:
        """
        Clears the current GUI widgets.
        """
        for widget in self.root.winfo_children():
            widget.destroy()
