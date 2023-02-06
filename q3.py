# Assignment week_4, question 3
from math import gcd


def lcm(*input):
    # This function returns the LCM value for 2 or more given inputs
    lcmm = input[0]
    for i in range(1,len(input)):
        lcmm = lcmm * input[i]//gcd(lcmm, input[i])
    return lcmm


print("Welcome to LCM calculator: ")

while True:
    try:
        user_input = []
        # take 4
        for i in range(1, 5):
            a = int(input("Enter input number " + str(i) + " : "))
            user_input.append(a)
    except ValueError:
        print("Invalid entry, please enter inegers")
        continue
    else:
        print("The LCM for the entered inputs is:", lcm(*user_input))
        break