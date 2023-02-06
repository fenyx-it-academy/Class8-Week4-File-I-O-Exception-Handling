
#Question 4

from add_function_file import add_function
from sub_function_file import sub_function
from divide_function_file import divide_function
from multiply_function_file import multiply_function
import math 

while True : 
    while 1 : 
        

        try: 
           number1 = float(input("please enter first number  : "))
           if type(number1) == float or type(number1) == int :
            break 
        except ValueError : 
            print("Sorry its not a number please try again :( ")

    while 1 : 
        try: 
            number2 = float(input("please enter second  number  : "))

            if type(number2) == float or type(number2) == int :
             break 
        except ValueError : 
            print("Sorry its not a number please try again :( ")
        
    user_choise = str(input("please choise one of this options  (+ , - , * , / ) :  "))
    if user_choise == "+" :
        result = add_function(number1 , number2) 
        print("Result : ",math.ceil(result))
    elif user_choise == "-" : 
        result = sub_function(number1 , number2)
        print("Result : ",math.ceil(result))
    elif user_choise == "*" : 
        result = multiply_function(number1 , number2)
        print("Result : ",math.ceil(result))
    elif user_choise == "/" : 
        result = divide_function(number1 , number2)
        print("Result : ",math.ceil(result))
    try_again = str(input("do you want to try again  (y/n) ?    "))
    if try_again != "y" : 
        break





