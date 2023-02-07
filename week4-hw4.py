import math

add = lambda x, y: float(x) + float(y)

sub = lambda x, y: float(x) - float(y) 

multi = lambda x, y: float(x) * float(y)

div = lambda x, y: float(x) / float(y)

print('''*************************************
Please choose which operation you want to do:

1) Addition 

2) Subtraction 

3) Multiplication 

4) Division
******************************''')

again = 'Y'
while again.upper() == 'Y':    

    try:
        choice = input('Your choice: ')
        assert 1 <= int(choice) <= 4
    
    except:
        print(("\nPlease enter a number between 1 and 4!!!\n"))        
    
    else:    
        try: 
            x = float(input('\nPlease enter first number: '))
            y = float(input('\nPlease enter second number: '))

            assert type(x) == float and type(y) == float

        except: 
            print("\nPlease enter a number!!!\n")

        else:             
            if choice == '1':
                print('\nThe result is ==> {}\n'.format(math.ceil(add(x, y))))                
                
            elif choice == '2':
                print('\nThe result is ==> {}\n'.format(math.ceil(sub(x, y))))

            elif choice == '3':
                print('\nThe result is ==> {}\n'.format(math.ceil(multi(x, y))))

            elif choice == '4':
                print('\nThe result is ==> {}\n'.format(math.ceil(div(x, y))))             
                             
    try:
        again = input('Do you want to contuine? (Y / N)\n')
        
        assert again.upper() == "N" or again.upper() == "Y"

    except:
        print("Please press 'Y' or 'N'!!!")  

    else: 
        if again.upper() == "N":
            break
        elif again.upper() == "Y":
            continue   