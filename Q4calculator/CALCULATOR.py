import math
from division import division 
from add import add 
from subtraction import sub 
from multiply import multiply
operations = {
    '/': division,
    '+': add,
    '-': sub,
    '*': multiply
}

#operation=input('Which operation do you want to use?Choose one of +,-,*,/')
while True:
    try:
        user_choosen_option=input('Which operation do you want to use?Choose one of +,-,*,/')
        assert user_choosen_option=="+"or user_choosen_option=="-" or user_choosen_option=="*" or user_choosen_option=="/"
        break
    except:
        print("Please choose correct operation")
        

while 1:
    try:
        number1=float(input("Enter first number"))
        number2=float(input("Enter second number"))
        assert type(number1)==float and type(number2)==float
        break
    except:
        print("Please enter only numbers")
        
if user_choosen_option == '+':
    print("result: ", add(number1, number2))

elif user_choosen_option == '-':
    print("result: ", sub(number1, number2))

elif user_choosen_option == '*':
    print("result: ", multiply(number1, number2))

elif user_choosen_option == '/':
    print("result: ", division(number1, number2))
            
        
        

    
    