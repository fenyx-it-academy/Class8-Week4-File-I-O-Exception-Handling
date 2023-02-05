import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
operations_directory = os.path.join(current_path, 'operations_functions\\')
sys.path.append(operations_directory)   # Adds the operations_functions directory to the Python path

# Imports the functions from the operations_functions directory
import add_function, sub_function, multiply_function, divide_function

def input_and_check(prompt, accepted_inputs, error_prompt='Error: Invalid input!'):
    ''' A function to check if the user input is in the accepted inputs. Returns the input if it is accepted. Otherwise, repeat.'''
    while True:
        input_string = input(prompt)
        try:
            if accepted_inputs == 'numbers':     # if the accepted input is a number (float)
                return float(input_string)
            else:
                assert input_string in accepted_inputs
                return input_string
        except (AssertionError, ValueError):
            print(error_prompt)


# The main loop
while True:
    number_1 = input_and_check('Enter first number: ', 'numbers', 'Error: Input must be a float value!')
    number_2 = input_and_check('Enter second number: ', 'numbers', 'Error: Input must be a float value!')
    operation = input_and_check('Choose an operation: [+, -, *, /]: ', ['+', '-', '*', '/'], 'Error: Invalid operation! Try again.')


    if operation == '+':
        print(f'{number_1} + {number_2} = {add_function.add(number_1, number_2)}')
    elif operation == '-':
        print(f'{number_1} - {number_2} = {sub_function.sub(number_1, number_2)}')
    elif operation == '*':
        print(f'{number_1} * {number_2} = {multiply_function.multiply(number_1, number_2)}')
    elif operation == '/':
        print(f'{number_1} / {number_2} = {divide_function.divide(number_1, number_2)}')
    
    if input_and_check('Do you want to continue? (Y/N): ', ['Y', 'y', 'N', 'n']).upper() == 'N':
        break

