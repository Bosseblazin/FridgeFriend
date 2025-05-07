import tkinter as tk

def input_validation(input_value):
    try:
        value = int(input_value)
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        return value
    except ValueError:
        error_window = tk.Toplevel()
        error_window.title("Input Error")
        error_window.geometry("300x100")
        tk.Label(error_window, text="Please enter a valid number greater than 0.").pack(padx=10, pady=10)
        return None