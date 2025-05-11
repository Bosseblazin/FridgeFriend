import tkinter as tk
from helpers import show_error

# Function to validate input
# This function will check if the input is a valid integer and greater than 0
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

# Function to validate item name
# This function will check if the item name is empty or contains invalid characters
# It will also convert the name to lowercase for consistency
def validate_item_name(name):
    cleaned_name = name.strip()
    if not cleaned_name:
        show_error("Item name cannot be empty.")
        return None
        # Restrict to alphabetic characters
    if not cleaned_name.replace(" ", "").isalpha():
        show_error("Item name must only contain letters and spaces.")
        return None
    return cleaned_name.lower()
