import tkinter as tk
from gui import CalculatorApp

def main() -> None:
    """
    Main function to initialize and start the application.
    """
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
