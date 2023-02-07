""" 
As a user, I want to use a program which can calculate basic  
mathematical operations. So that I can add, subtract, multiply or divide my inputs.

**Acceptance Criteria:**

* The calculator must support the Addition, Subtraction, Multiplication and  Division operations.
* Define four functions in four files for each of them, with two float numbers as parameters.
* To calculate the answer, use math.ceil()  and get the next integer value greater than the result
* Create a menu using the print command with the respective options and take an input user_choosen_option from the user.
* Using if/elif statements for cases and call the appropriate functions.
* Use try/except blocks to verify input entries and warn the user for incorrect inputs.
* Ask user if calculate numbers again. To implement this, take the input from user `Y` or `N`.
 """


from func_add import *
from func_divide import *
from func_multiply import *
from func_subtract import *


while True:

    print("What do you want to do: ")
    print("(a) add")
    print("(s) subtract")
    print("(m) multiply")
    print("(d) divide")
    
    user_choosen_option = input("Enter first letter...  (a)dd, (s)ubtract, (m)ultiply, or  (d)ivide: ")

    try:
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))
        if user_choosen_option == 'a':
            print("result: ", add(num1, num2))

        elif user_choosen_option == 's':
            print("result: ", subtract(num1, num2))

        elif user_choosen_option == 'm':
            print("result: ", multiply(num1, num2))

        elif user_choosen_option == 'd':
            print("result: ", divide(num1, num2))
            
    except ValueError:
        print("there's an input error")

    calculate_again = input("do you want to calculate something else? (y)es or (n)o? ")
    if calculate_again != "y":
        break
