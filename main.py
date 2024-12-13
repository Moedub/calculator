### main.py ###
import tkinter as tk
from tkinter import ttk
from gui import create_calculator_gui
from calculator import create_area_gui

def main():
    window = tk.Tk()
    window.title("Calculator with Area Functions")

    # Set up style for the window
    style = ttk.Style(window)
    style.theme_use("clam")

    # White background for a calm theme
    window.configure(bg="white")

    # Create the main calculator GUI
    create_calculator_gui(window)

    # Flag to track if the area window is open
    area_window_open = [False]  # Use a list to allow modification inside lambda functions

    # Button to toggle between area functions and the calculator
    def toggle_area_window():
        if area_window_open[0]:
            # Close the area window
            for widget in window.winfo_children():
                if isinstance(widget, tk.Toplevel):  # Check if widget is a Toplevel (area window)
                    widget.destroy()
            area_window_open[0] = False
        else:
            # Open the area window
            create_area_gui(window)
            area_window_open[0] = True

    fx_button = tk.Button(window, text="fx", width=10, height=2, font=("Arial", 14),
                          bg="#d1e7ff", fg="black", command=toggle_area_window)
    fx_button.grid(row=5, column=4, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()




