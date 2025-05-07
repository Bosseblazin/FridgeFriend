import json
import os

inventory_file = "inventory.json"

def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as file:
            return json.load(file)
    return {}

def save_inventory(inventory):
    with open(inventory_file, "w") as file:
        json.dump(inventory, file, indent=4)

def show_confirmation(title, message):
    import tkinter as tk
    window = tk.Toplevel()
    window.title(title)
    window.geometry("350x150")
    tk.Label(window, text=message, wraplength=200).pack(padx=10, pady=10)