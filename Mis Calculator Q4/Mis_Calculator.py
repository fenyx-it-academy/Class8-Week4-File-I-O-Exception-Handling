# Assignment week 4, question 1

from Addition import add
from Multiplication import Multiply
from Substraction import substract
from Division import divide

def greetings_and_instructions():
    # Instructions to the user
    print('Choose one of the following operations: ')
    print('1- For Addition')
    print('2- For Subtraction')
    print('3- For Multiplication')
    print('4- For Division')
    
    
print('Welcome to Mis Calculator')
greetings_and_instructions()


while True:
    try:
        user_choice = int(input('\nYour choice: '))
        assert user_choice > 0 and user_choice <= 4
    except ValueError:
        print('You entered wrong choice, please choose again as displayed in the menu: ')
        greetings_and_instructions()
        continue
    except AssertionError:
        print('Your choice is not within the menu, please choose again as displayed in the menu: ')   
        greetings_and_instructions()
        continue
    
    while True:
        try:
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
        except ValueError:
            print('You did not enter a number, please enter a number:\n')
            continue
        else: 
            break
        
     
    
    if user_choice == 1:
        print(a,'+',b ,'=',add(a,b))
    elif user_choice == 2:
        print(a,'-',b ,'=',substract(a,b))
    elif user_choice == 3:
        print(a,'*',b ,'=',Multiply(a,b))
    elif user_choice == 4:
        print(a,'/',b ,'=',divide(a,b))
        
    repeat = input('Do you want to repeat? (Yes), (Y) or (No) (N): ').upper()
    
    if repeat == 'Y' or repeat == 'YES':
        greetings_and_instructions()
        continue
    if repeat != 'Y' or repeat != 'YES':
        break
    
print('Thank you! ')