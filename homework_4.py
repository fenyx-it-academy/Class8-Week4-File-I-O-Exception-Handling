### Question 4 
""""" Mis Calculator
As a user, I want to use a program which can calculate basic mathematical operations. So that I can add, subtract, multiply or divide my inputs.

Acceptance Criteria:

The calculator must support the Addition, Subtraction, Multiplication and Division operations.
Define four functions in four files for each of them, with two float numbers as parameters.
To calculate the answer, use math.ceil()  and get the next integer value greater than the result
Create a menu using the print command with the respective options and take an input choice from the user.
Using if/elif statements for cases and call the appropriate functions.
Use try/except blocks to verify input entries and warn the user for incorrect inputs.
Ask user if calculate numbers again. To implement this, take the input from user Y or N."""""


from my_modules import *

# Define the main function
def main_func():
    
    while True:
        
        choice = input(""" Enter Your choice if you want to 
                       for Addition write = add,
                       for Subtraction= sub,
                       for Multiplication = mult,
                       for Division= div,
                       :> """).lower()
        
        # Try to retrieve the two numbers from the user input
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
       
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Check the user's choice and call the appropriate function from the imported module
        if choice == "add":
            r = add(num1, num2)
            print("The result is ", r)
        elif choice == "sub":
            r = subtract(num1, num2)
            print("The result is ", r)
        elif choice == "mult":
            r = multiply(num1, num2)
            print("The result is ", r)
        elif choice == "div":
            r = divide(num1, num2)
            print("The result is ", r)
        # If the user's choice is invalid, show an error message and prompt again
        else:
            print("Invalid choice. Please try again.")
            continue
        
        # Ask the user if they want to calculate again
        t = input("Do you want to calculate again? (y/n): ").lower()
        # If the user doesn't want to calculate again, break out of the loop
        if t != 'y':
            break

# Execute the main function when the script is run as the main program
if __name__ == "__main__":
    main_func()