import tkinter as tk
from inventory import addition, subtraction
from validation import input_validation, validate_item_name
from helpers import load_inventory, show_error
from tkinter import PhotoImage
import os

#Define the functions for adding and subtracting items from the inventory
#These functions will create a new window for the user to input the item and quantity
def add_item():
    add_item_window = tk.Toplevel()
    add_item_window.title("Add Items")
    add_item_window.geometry("300x200")

    tk.Label(add_item_window, text="What would we like to add?").grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    item_entry = tk.Entry(add_item_window)
    item_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_item_window, text="How many would we like to add?").grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    quantity_entry = tk.Entry(add_item_window)
    quantity_entry.grid(row=3, column=1, padx=10, pady=5)

    #Function to send submition to the addition function
    #This function will validate the item name and quantity before calling the addition function
    def on_submit():
        item_name = validate_item_name(item_entry.get())
        quantity = input_validation(quantity_entry.get())
        if item_name and quantity:
            addition(item_name, quantity, add_item_window)

    tk.Button(add_item_window, text="Submit", command=on_submit).grid(row=4, column=1, padx=2, pady=10)

#Define the function for subtracting items from the inventory
def subtract_item():
    subtract_item_window = tk.Toplevel()
    subtract_item_window.title("Subtract Items")
    subtract_item_window.geometry("300x200")

    tk.Label(subtract_item_window, text="What would we like to subtract?").grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    item_entry = tk.Entry(subtract_item_window)
    item_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(subtract_item_window, text="How many would we like to subtract?").grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    quantity_entry = tk.Entry(subtract_item_window)
    quantity_entry.grid(row=3, column=1, padx=10, pady=5)

    #Function to send submition to the subtraction function
    #This function will validate the item name and quantity before calling the subtraction function
    def on_submit():
        item_name = validate_item_name(item_entry.get())
        quantity = input_validation(quantity_entry.get())
        if item_name and quantity:
            subtraction(item_name, quantity, subtract_item_window)

    tk.Button(subtract_item_window, text="Submit", command=on_submit).grid(row=4, column=1, padx=2, pady=10)


#Define the function for viewing the inventory
#This function will create a new window to display the current inventory
def view_list():
    view_list_window = tk.Toplevel()
    view_list_window.title("View Inventory")
    view_list_window.geometry("150x500")

    inventory = load_inventory()
    # Sort the inventory by item name
    # This will ensure that the items are displayed in alphabetical order
    sorted_inventory = sorted(inventory.items(), key=lambda x: x[0])
    inventory_list = "\n".join([f"{item}: {quantity}" for item, quantity in sorted_inventory])
    tk.Label(view_list_window, text="Current Inventory:").grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    tk.Label(view_list_window, text=inventory_list).grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    tk.Button(view_list_window, text="Close", command=view_list_window.destroy).grid(row=2, column=1, padx=2, pady=10)

#Create the main window for the application
#This window will contain the buttons for adding, subtracting, and viewing the inventory
app = tk.Tk()
app.title("FridgeFriend")
app.geometry("400x320")
fidge_img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "fridge.png"))
grocery_img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "groceries.png"))
shopping_cart_img = PhotoImage(file=os.path.join(os.path.dirname(__file__), "shopping.png"))

#Load the images for the fridge, grocery list, and shopping cart
shopping_label = tk.Label(app, image=shopping_cart_img)
shopping_label.image = shopping_cart_img
shopping_label.grid(row=0, column=0, padx=10, pady=10)
tk.Label(app, text="Shopping Cart").grid(row = 1, column = 0, padx=10, pady=10)
fridge_label = tk.Label(app, image=fidge_img)
fridge_label.image = fidge_img
fridge_label.grid(row=0, column=2, padx=10, pady=10)
tk.Label(app, text="Fridge").grid(row = 1, column = 2, padx=10, pady=10)
grocery_label = tk.Label(app, image=grocery_img)
grocery_label.image = grocery_img
grocery_label.grid(row=0, column=1, padx=10, pady=10)
tk.Label(app, text="Grocery List").grid(row = 1, column = 1, padx=10, pady=10)

#Add an attribution label to the bottom of the window
#This label will display the source of the images used in the application
attribution = tk.Label(app, text="Images by Pixabay & Vecteezy. Used under license.", font=("Arial", 8))
attribution.grid(row=4, column=0, columnspan=2, pady=(5, 15))

#Create the buttons for adding, subtracting, and viewing the inventory
tk.Label(app, text="Hello, What would we like to do today?").grid(row=2, column=0, columnspan=3, padx=10, pady=10)
tk.Button(app, text="Add Inventory", command=add_item).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
tk.Button(app, text="Subtract Inventory", command=subtract_item).grid(row=3, column=1, padx=5, pady=5, sticky="ew")
tk.Button(app, text="View Inventory", command=view_list).grid(row=3, column=2, padx=5, pady=5, sticky="ew")
tk.Button(app, text="Exit", command=app.quit).grid(row=5, column=1, padx=5, pady=5, sticky="ew")

#Run the main loop to display the application
app.mainloop()