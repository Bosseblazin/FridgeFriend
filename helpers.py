import json
import os
import tkinter as tk

inventory_file = "inventory.json"

# Function to load the inventory from a JSON file
# This function will read the inventory from a JSON file and return it as a dictionary
# If the file does not exist, it will return an empty dictionary
def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as file:
            return json.load(file)
    return {}

# Function to save the inventory to a JSON file
def save_inventory(inventory):
    with open(inventory_file, "w") as file:
        json.dump(inventory, file, indent=4)

# Function to show a confirmation message
def show_confirmation(title, message):
    import tkinter as tk
    window = tk.Toplevel()
    window.title(title)
    window.geometry("350x150")
    tk.Label(window, text=message, wraplength=200).pack(padx=10, pady=10)

# Function to show an error message
# This function will create a new window to display an error message
def show_error(message):
    error_window = tk.Toplevel()
    error_window.title("Input Error")
    error_window.geometry("300x100")
    tk.Label(error_window, text=message).pack(padx=10, pady=10)
