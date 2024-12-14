import tkinter as tk
import math

def on_button_click(entry: tk.Entry, value: str) -> None:
    """
    Handle button click events for numeric and operator buttons.

    Args:
        entry: The entry widget where the expression is displayed.
        value: The button value to be added to the entry.
    """
    entry.insert(tk.END, value)

def on_clear(entry: tk.Entry) -> None:
    """
    Clear the content of the entry widget.

    Args:
        entry: The entry widget to clear.
    """
    entry.delete(0, tk.END)

def on_delete(entry: tk.Entry) -> None:
    """
    Delete the last character from the entry widget.

    Args:
        entry: The entry widget to modify.
    """
    entry.delete(len(entry.get()) - 1, tk.END)

def on_equal(entry: tk.Entry) -> None:
    """
    Evaluate the expression in the entry widget and display the result.

    Args:
        entry: The entry widget containing the expression to evaluate.
    """
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_area(shape: str, dim1: str, dim2: str, result_label: tk.Label) -> None:
    """
    Calculate the area based on the selected shape and dimensions.

    Args:
        shape: The selected shape for area calculation.
        dim1: The first dimension input (e.g., radius or base).
        dim2: The second dimension input (e.g., height or None for Circle/Square).
        result_label: Label widget to display the area result.
    """
    try:
        dimension1 = float(dim1)
        dimension2 = float(dim2) if dim2 else None

        if shape == "Circle":
            area = math.pi * (dimension1 ** 2)
        elif shape == "Rectangle":
            area = dimension1 * dimension2
        elif shape == "Triangle":
            area = 0.5 * dimension1 * dimension2
        elif shape == "Square":
            area = dimension1 ** 2
        else:
            result_label.config(text="Invalid Shape")
            return

        result_label.config(text=f"Area = {area:.2f}")
    except (ValueError, TypeError):
        result_label.config(text="Error: Invalid input")

def create_calculator_gui(window: tk.Tk) -> None:
    """
    Create the calculator GUI within the main application window.

    Args:
        window: The main application window.
    """
    window.title("Calculator Project")
    window.geometry("400x600")

    # Entry widget for standard calculations
    entry = tk.Entry(window, width=20, font=("Arial", 24), bg="white", bd=10, relief="solid", justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Result label for area calculations (non-editable)
    result_label = tk.Label(window, text="", font=("Arial", 18), bg="white", fg="black", anchor="w", width=20, relief="solid")

    # Shape selection (radio buttons)
    shape_var = tk.StringVar(value="Circle")
    shapes = ["Circle", "Rectangle", "Triangle", "Square"]
    shape_buttons = []
    for idx, shape in enumerate(shapes):
        button = tk.Radiobutton(window, text=shape, variable=shape_var, value=shape, font=("Arial", 12), bg="white", fg="black")
        shape_buttons.append(button)

    # Dimension input fields
    dim1_label = tk.Label(window, text="Base / Radius:", font=("Arial", 12), bg="white", fg="black")
    dim1_entry = tk.Entry(window, font=("Arial", 14), bd=5, relief="solid", width=10)

    dim2_label = tk.Label(window, text="Height:", font=("Arial", 12), bg="white", fg="black")
    dim2_entry = tk.Entry(window, font=("Arial", 14), bd=5, relief="solid", width=10)

    # Submit button for area calculation
    submit_button = tk.Button(window, text="Submit", font=("Arial", 14), bg="#d1e7ff", fg="black", command=lambda: calculate_area(shape_var.get(), dim1_entry.get(), dim2_entry.get(), result_label))

    # Selected field to direct inputs in Area Mode
    selected_field = tk.StringVar(value="dim1")

    def handle_area_mode_input(value: str):
        """
        Handle button input for Base/Radius or Height fields in Area Calculation Mode.

        Args:
            value: The value of the button pressed.
        """
        if selected_field.get() == "dim1":
            dim1_entry.insert(tk.END, value)
        elif selected_field.get() == "dim2":
            dim2_entry.insert(tk.END, value)

    def clear_selected_field():
        """Clear the currently selected field."""
        if selected_field.get() == "dim1":
            dim1_entry.delete(0, tk.END)
        elif selected_field.get() == "dim2":
            dim2_entry.delete(0, tk.END)

    def delete_selected_field():
        """Delete the last character from the currently selected field."""
        if selected_field.get() == "dim1":
            dim1_entry.delete(len(dim1_entry.get()) - 1, tk.END)
        elif selected_field.get() == "dim2":
            dim2_entry.delete(len(dim2_entry.get()) - 1, tk.END)

    # Calculator buttons
    buttons = [
        ('7', 5, 0), ('8', 5, 1), ('9', 5, 2),
        ('4', 6, 0), ('5', 6, 1), ('6', 6, 2),
        ('1', 7, 0), ('2', 7, 1), ('3', 7, 2),
        ('0', 8, 0), ('.', 8, 1), ('+', 5, 3), ('-', 6, 3),
        ('*', 7, 3), ('/', 8, 3), ('Clear', 9, 0), ('Del', 9, 1), ('=', 9, 2)
    ]

    for (text, row, col) in buttons:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), bg="#d9f7be", fg="black",
                           relief="raised",
                           command=lambda value=text: (
                               handle_area_mode_input(value) if result_label.winfo_ismapped() and value not in ['Clear', 'Del', '='] else (
                                   clear_selected_field() if result_label.winfo_ismapped() and value == 'Clear' else (
                                       delete_selected_field() if result_label.winfo_ismapped() and value == 'Del' else (
                                           on_button_click(entry, value) if not result_label.winfo_ismapped() and value not in ['Clear', 'Del', '='] else (
                                               on_clear(entry) if not result_label.winfo_ismapped() and value == 'Clear' else (
                                                   on_delete(entry) if not result_label.winfo_ismapped() and value == 'Del' else (
                                                       on_equal(entry) if not result_label.winfo_ismapped() and value == '=' else None
                                                   )
                                               )
                                           )
                                       )
                                   )
                               )
                           ))
        button.grid(row=row, column=col, padx=5, pady=5)

    # Toggle button for switching modes
    def toggle_mode():
        if result_label.winfo_ismapped():
            result_label.grid_remove()
            entry.grid()
            for widget in shape_buttons + [dim1_label, dim1_entry, dim2_label, dim2_entry, submit_button]:
                widget.grid_remove()
        else:
            result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
            entry.grid_remove()
            for idx, button in enumerate(shape_buttons):
                button.grid(row=2, column=idx)
            dim1_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
            dim1_entry.grid(row=3, column=1, padx=5, pady=5)
            dim2_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
            dim2_entry.grid(row=4, column=1, padx=5, pady=5)
            submit_button.grid(row=3, column=2, rowspan=2, padx=5, pady=5)

    mode_button = tk.Button(window, text="Mode", font=("Arial", 14), bg="#f7d9d9", fg="black", command=toggle_mode)
    mode_button.grid(row=9, column=3, padx=5, pady=5)

    # Click handlers to select input fields
    dim1_entry.bind("<FocusIn>", lambda _: selected_field.set("dim1"))
    dim2_entry.bind("<FocusIn>", lambda _: selected_field.set("dim2"))

    # Grid configuration
    for i in range(10):
        window.grid_rowconfigure(i, weight=1)
    for i in range(4):
        window.grid_columnconfigure(i, weight=1)
