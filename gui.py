import tkinter as tk
from tkinter import ttk

def on_button_click(entry, value):
    entry.insert(tk.END, value)

def on_clear(entry):
    entry.delete(0, tk.END)

def on_delete(entry):
    entry.delete(len(entry.get()) - 1, tk.END)

def on_equal(entry):
    try:
        result = str(eval(entry.get()))  # Evaluates the string as a Python expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def create_calculator_gui(window):
    # Entry widget with larger size and clean theme
    entry = tk.Entry(window, width=20, font=("Arial", 24), bg="white", bd=10, relief="solid", justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

    # Buttons with modern styling
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
        ('0', 4, 0), ('+', 1, 3), ('-', 2, 3),
        ('*', 3, 3), ('/', 4, 3), ('Clear', 4, 1),
        ('Del', 4, 2), ('=', 5, 0, 4)
    ]

    for (text, row, col, *span) in buttons:
        span = tuple(span) if span else (1, 1)
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), bg="#d9f7be", fg="black",
                           relief="raised",
                           command=lambda value=text: on_button_click(entry, value) if value not in ['Clear', 'Del',
                                                                                                     '='] else (
                               on_clear(entry) if value == 'Clear' else (
                                   on_delete(entry) if value == 'Del' else on_equal(entry))))
        button.grid(row=row, column=col, columnspan=span[0], padx=10, pady=10, sticky="nsew")

    # Make the grid columns/rows expand to fit the buttons
    for i in range(6):
        window.grid_rowconfigure(i, weight=1)
    for i in range(4):
        window.grid_columnconfigure(i, weight=1)
