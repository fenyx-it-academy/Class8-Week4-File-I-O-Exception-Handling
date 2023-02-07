### Question 3
"""As a user, I want to use a program which can calculate the least common multiple (L.C.M.) 
of four numbers. So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria:

Ask user to enter the four numbers.
Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
Calculate the least common multiple (L.C.M.) of four numbers
Use gcd function in module of math
"""

import math

"""The 'main_func' function takes four numbers as input and returns the L.C.M. of these numbers."""
def main_func(num1,num2,num3,num4):
    #  Code that should be executed when the script is run as the main program
    """The 'math.gcd' function from the 'math' library to calculate the greatest common divisor of two numbers, 
    which is then used to calculate the L.C.M."""
    return num1 * num2 * num3 * num4 // math.gcd(math.gcd(num1, num2), math.gcd(num3, num4))


"""The code is executed only when the script is run as the main program, as 
determined by the 'if name == 'main':' statement. Within this block, user input is obtained 
for the four numbers and the 'main_func' is called with these inputs. The result is then printed to 
the console. Exception handling is used to ensure that the input is a valid number.
"""
if __name__ == '__main__':
    
    while True:
        try:
            n1 = int(input("Enter the first number:"))
            n2 = int(input("Enter the seconde number:"))
            n3 = int(input("Enter the third number:"))
            n4 = int(input("Enter the fourth number:"))
            break
        except:
            print("Invalid input. Pleass enter a number.")

    r = main_func(n1, n2, n3, n4)
    print("The least common multiple (L.C.M.) of four numbers:", r)
    
    
    
    

    
    
