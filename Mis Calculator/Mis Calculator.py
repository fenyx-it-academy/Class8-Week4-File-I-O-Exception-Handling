import Add_C, Subt_C, Mul_C, Div_C

def print_menu():
    print("\n************")
    print("1 - Add   ")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("************")
    
def valid_choice():
    # this function returns validated mathematical operation choice as integer code from the menu above
    while True:
        print_menu()
        try:
            op_no = input("\nWhich calculation? (1--4) : ")
            if op_no in str(list(range(1,5))):
                return int(op_no)
                break
            else:
                raise ValueError("\nInvalid value as choice!\n")
        except ValueError as ve:
            print(ve)


def valid_input(num):
    # this function returns validated operands for calculation
    while True:  
        a = input(f"{num}. number :")
        try:
            return float(a)
            break
        except ValueError:
            print ("Not a float\n")
    
def keep_going():
    while True:
        decision = input("\nWould you like to go on? (Y/N)  : ")
        try:
            if decision.lower() in ["y", "yes"]:
                return True
            elif decision.lower() in ["n", "no"]:
                return False
            else:
                raise ValueError("Choice is not Y or N")
            break
        except ValueError as ve:
            print (ve)

while True:
    op_no = valid_choice()  # if the valid operation choice succesful
    num1 = valid_input(1)
    num2 = valid_input(2)
    if op_no == 1:
        result = Add_C.add(num1, num2)
    elif op_no == 2:
        result = Subt_C.subtract(num1, num2)
    elif op_no == 3:
        result = Mul_C.multiply(num1, num2)
    elif op_no == 4:
        result = Div_C.divide(num1, num2)
    print (f"Result : {result}")
    if keep_going() == False:
        break