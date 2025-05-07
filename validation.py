import tkinter as tk

#Validate user input for adding or subtracting items
def input_validation(input_value, food_item):
    #Validate the value entered by the user by checking if it is greater than 0
    try:
        value = int(input_value)
        if value <= 0:
            raise ValueError("Value must be greater than 0")
    except ValueError:
        error_window = tk.Toplevel()
        error_window.title("Input Error")
        error_window.geometry("300x100")
        tk.Label(error_window, text="Please enter a valid number greater than 0.").pack(padx=10, pady=10)
        return None

#Validate the food item entered by the user by checking if it is not empty
    try:
        if food_item.strip() == "":
            raise ValueError("Food item cannot be empty")
    except ValueError:
        error_window = tk.Toplevel()
        error_window.title("Input Error")
        error_window.geometry("300x100")
        tk.Label(error_window, text="Please enter a valid food item.").pack(padx=10, pady=10)
        return None

    return value, food_item