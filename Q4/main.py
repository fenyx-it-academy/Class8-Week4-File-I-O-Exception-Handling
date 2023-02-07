import math
from addition import add
from subtraction import sub
from multiplication import multi
from division import div


i = "Y"
while i == "Y":
    while True:
        try:
            num1 = float(input("\nEnter the first number:"))
            num2 = float(input("Enter the second number:"))
            break
        except ValueError:
            print("Value can't be empty or non numerical")

    print(
        "\nSelect operation:(You can select by pressing the number next to the operation)")
    print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Divison\n")
    while True:
        try:
            select = int(input("Enter your choice:"))
            assert select in [1, 2, 3, 4]
            break
        except:
            print(
                "Invalid input, Value can't be empty or non numerical, Make sure you select the correct number of the operation"
            )

    if select == 1:
        result = add(num1, num2)
    elif select == 2:
        result = sub(num1, num2)
    elif select == 3:
        result = multi(num1, num2)
    else:
        result = div(num1, num2)

    print("\nThe result is:", math.ceil(result))
    while True:
        try:
            i = input("\nPress 'Y to continue or 'N to exit': ").upper()
            assert i in ["Y", "N"]
            break
        except:
            print("Please enter either 'Y' or 'N'")
