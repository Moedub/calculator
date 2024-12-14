import tkinter as tk
from gui import create_calculator_gui

def main() -> None:
    """
    Main function to initialize the Calculator application.
    It sets up the GUI and handles toggling between the calculator and area functions.
    """
    window = tk.Tk()
    window.title("Calculator App")

    # Set up the calculator GUI
    create_calculator_gui(window)

    # Run the main loop
    window.mainloop()

if __name__ == "__main__":
    main()