from tkinter import ttk
from Arthimetics import* # all the arthimetic functions are in one file.
import tkinter as tk
def calculator():
    """A function that accepts two numbers and an operator from the user input fields
       and perform the chosen operation on the two operands. Then display the result on 
       the screen"""
    try:
       number_1 = float(number_1_entry.get())
       number_2 = float(number_2_entry.get())
    except ValueError:
        print(result_display.config(text="Error! please enter a number"))
    else:
        operator = list_down.get()
        if operator == "Addition":
            result = addition(number_1,number_2)
        elif operator == "Subtruction":
            result = subtruction(number_1,number_2)
        elif operator == "Multiplication":
             result = multiplication(number_1,number_2)
        else:
            result = division(number_1,number_2)
        result_display.config(text= result)

root = tk.Tk()
root.title("Simple Calculator")

number_1_label = tk.Label(root, text="Enter First Number")
number_1_label.grid(row= 0, column= 0, pady=10)
number_1_entry = tk.Entry(root)
number_1_entry.grid(row=0, column=1)

number_2_label = tk.Label(root, text="Enter Second Number")
number_2_label.grid(row= 1, column= 0)
number_2_entry = tk.Entry(root)
number_2_entry.grid(row=1, column=1)
result_label = tk.Label(root, text="  =  ")
result_label.grid(row= 2, column= 2)
result_display = tk.Label(root, text="")
result_display.grid(row=2, column=3)

options = ["Addition","Subtruction","Multiplication","Division"] # list of operators to be chosen by the user.
choose_arithmetic_label = tk.Label(root, text = "Choose an Operator ")
choose_arithmetic_label.grid(row= 3, column= 0)
list_down = ttk.Combobox(state= "readonly", values=options) 
list_down.grid(row= 3, column= 1)
generate_button = tk.Button(root, text="Go", command=calculator)
generate_button.grid(row=4, column=1, columnspan=1,pady=10)

root.mainloop()

