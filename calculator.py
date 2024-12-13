import tkinter as tk
import math

def on_area_submit(entry1, entry2, shape, result_label):
    if shape == "Select Shape":
        result_label.config(text="Please select a shape")
        return

    try:
        dimension1 = float(entry1.get())
        dimension2 = float(entry2.get()) if entry2.get() else None

        if shape == "Circle":
            result = math.pi * (dimension1 ** 2)  # Circle area: πr²
        elif shape == "Rectangle":
            result = dimension1 * dimension2  # Rectangle area: length * width
        elif shape == "Triangle":
            result = 0.5 * dimension1 * dimension2  # Triangle area: 0.5 * base * height
        elif shape == "Square":
            result = dimension1 ** 2  # Square area: side²
        else:
            result = "Invalid shape"

        result_label.config(text=f"Area: {result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

def create_area_gui(window):
    area_window = tk.Toplevel(window)
    area_window.title("Area Functions")
    area_window.configure(bg='white')  # Background color

    shape_var = tk.StringVar(value="Select Shape")

    # Radio buttons for selecting shapes
    tk.Label(area_window, text="Select shape:", font=("Arial", 14), bg='white', fg="black").grid(row=0, column=0,
                                                                                                   padx=10, pady=5)
    tk.Radiobutton(area_window, text="Circle", variable=shape_var, value="Circle", font=("Arial", 12), bg='white',
                   fg="black").grid(row=0, column=1)
    tk.Radiobutton(area_window, text="Rectangle", variable=shape_var, value="Rectangle", font=("Arial", 12),
                   bg='white', fg="black").grid(row=0, column=2)
    tk.Radiobutton(area_window, text="Triangle", variable=shape_var, value="Triangle", font=("Arial", 12), bg='white',
                   fg="black").grid(row=0, column=3)
    tk.Radiobutton(area_window, text="Square", variable=shape_var, value="Square", font=("Arial", 12), bg='white',
                   fg="black").grid(row=0, column=4)

    # Entry widgets for dimensions
    tk.Label(area_window, text="Enter Dimension 1 (Radius/Base):", font=("Arial", 12), bg='white', fg="black").grid(
        row=1, column=0, padx=10, pady=5)
    entry1 = tk.Entry(area_window, font=("Arial", 14), bd=5, relief="solid")
    entry1.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(area_window, text="Enter Dimension 2 (Height/Width):", font=("Arial", 12), bg='white', fg="black").grid(
        row=2, column=0, padx=10, pady=5)
    entry2 = tk.Entry(area_window, font=("Arial", 14), bd=5, relief="solid")
    entry2.grid(row=2, column=1, padx=10, pady=5)

    # Result label
    result_label = tk.Label(area_window, text="Area: ", font=("Arial", 16), bg='white', fg="black")
    result_label.grid(row=4, column=0, columnspan=5, pady=10)

    # Submit button
    submit_button = tk.Button(area_window, text="Submit", font=("Arial", 14), bg="#d1e7ff", fg="black",
                              command=lambda: on_area_submit(entry1, entry2, shape_var.get(), result_label))
    submit_button.grid(row=5, column=0, columnspan=5, pady=10)
