###  Mis Calculator
from ceil_add import *
from ceil_div import *
from ceil_mult import *
from ceil_sub import *

def operation():
    while True:
        user_choice = input (" Enter Your choice as follows: for Summation please write = (sum), for Subtraction= (sub), for Multiplication = (mul), for Division= (div):> ").lower()
        try:        # Using try/except block to verify input entries and warn the user for incorrect inputs.
            number_1 = float(input("Enter your first number: "))  # two parameters are float numbers  
            number_2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid Input Error: Please enter a number!")
            continue
# Check the user's choice and call the appropriate function from the imported module
        if user_choice == "sum":
            result = addition(number_1, number_2)
            print("Summation of the two numbers is: ", result)
        elif user_choice == "sub":
            result = subtruction(number_1, number_2)
            print("Subtruction of the two numbers is: ", result)
        elif user_choice == "mul":
            result = multiplication(number_1, number_2)
            print("Multiplication of the two numbers is: ", result)
        elif user_choice == "div":
            result = division(number_1, number_2)
            print("Division of the two numbers is: ", result)
        #  except:
        #     number_2 ==0 
        #     break
        #     print("ZeroDivisionError because number_2 should not be zero!!! ")
        else:                      # warnning the user for incorrect inputs.
            print("You entered something wrong! Invalid choice.")
            continue
        calc_again = input("If you want to use the Mis Calculator again, please type upper letter of the first word Yes or No (Y/N): ").upper()         # Ask the user if he/ she wants to use the calculater again
        if calc_again == 'N':
            break
if __name__ == "__pycache__":
    operation()