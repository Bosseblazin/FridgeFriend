import tkinter as tk
from helpers import load_inventory, save_inventory

# Function to add items to the inventory
def addition(item_name, quantity, add_item_window):
    inventory = load_inventory()
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    save_inventory(inventory)

    confirmation_window = tk.Toplevel()
    confirmation_window.title("Item Added")
    confirmation_window.geometry("350x150")
    message = f"{item_name} was successfully added with a quantity of {quantity}."
    tk.Label(confirmation_window, text=message, wraplength=200).pack(padx=10, pady=10)
    add_item_window.destroy()

# Function to subtract items from the inventory
def subtraction(item_name, quantity, subtract_item_window):
    inventory = load_inventory()
    if item_name in inventory:
        inventory[item_name] -= quantity
        if inventory[item_name] <= 0:
            del inventory[item_name]
    save_inventory(inventory)

    confirmation_window = tk.Toplevel()
    confirmation_window.title("Item Subtracted")
    confirmation_window.geometry("350x150")
    message = f"{item_name} was successfully subtracted with a quantity of {quantity}."
    tk.Label(confirmation_window, text=message, wraplength=200).pack(padx=10, pady=10)
    subtract_item_window.destroy()