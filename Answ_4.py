## 4- Mis Calculator

# As a user, I want to use a program which can calculate basic 
#  mathematical operations. So that I can add, subtract, 
#  multiply or divide my inputs.

# **Acceptance Criteria:**

# * The calculator must support the Addition, Subtraction, Multiplication 
# and  Division operations.
# * Define four functions in four files for each of them, with two float 
# numbers as parameters.
# * To calculate the answer, use math.ceil()  and get the next integer 
# value greater than the result
# * Create a menu using the print command with the respective options 
# and take an input choice from the user.
# * Using if/elif statements for cases and call the appropriate functions.
# * Use try/except blocks to verify input entries and warn the user 
# for incorrect inputs.
# * Ask user if calculate numbers again. To implement this, take the 
# input from user `Y` or `N`.

from Add_calc import *
from Divis_calc import *
from Mult_calc import *
from Substr_calc import *

actions = {
    '/': divis,
    '+': addition,
    '-': substract,
    '*': multipl
}

while True:
    try:
        print('\n\n Hello to Mis Calculator!\n')
        a = float(input('Enter first number -'))
        b = float(input('Enter second number -'))
   

        action = input('''Chose the action. 
        Enter character: 
        + for add
        - for subtract
        * for multiply
        / for divide''')
        assert action in actions
        print(f'The result is {(actions[action](a,b))}') 
    except ValueError as e:
        print()
        print('Enter number only!')
        print()
    except AssertionError:
        print()
        print('Unavailable action.')

    answer = input('Whould you like to continue? Y or N... ')
    if answer.lower() in 'yes':
        continue
    else:
        break 
