import json
import os

#initialize the inventory file
inventory_file = "inventory.json"

#Check if the inventory file exists and load it, if not create an empty inventory
def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as file:
            return json.load(file)
    return {}

#Save the inventory to the file
def save_inventory(inventory):
    with open(inventory_file, "w") as file:
        json.dump(inventory, file, indent=4)

#Confirmation window for successful addition or subtraction of items
def show_confirmation(title, message):
    import tkinter as tk
    window = tk.Toplevel()
    window.title(title)
    window.geometry("350x150")
    tk.Label(window, text=message, wraplength=200).pack(padx=10, pady=10)