import tkinter as tk

def add_item(item):
    print("Added Item")
    return

def subtract_item(item):
    print("Subtracted Item")
    return

def view_list():
    print("Inventory printed")
    return

#Main application window
app = tk.Tk()

#Set the title of the window
app.title("FridgeFriend")
app.geometry("375x200") #Set the size of the window

#add a label
tk.Label(app, text = "Hello, Welcome to the main menu what would we like to do today?").grid(row = 0, column = 0)


#add buttons
tk.Button(app, text = "Add Inventory", command = lambda: add_item("Add Inventory")).grid(row = 1, column = 0, padx = 10, pady = 10)
tk.Button(app, text = "Subtract Inventory", command = lambda: subtract_item("Add Inventory")).grid(row = 2, column = 0, padx = 10, pady = 10)
tk.Button(app, text = "View Inventory", command = lambda: view_list("Add Inventory")).grid(row = 3, column = 0, padx = 10, pady = 10)

#Enter main loop
app.mainloop()
