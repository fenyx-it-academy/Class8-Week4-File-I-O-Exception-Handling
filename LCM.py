## LCM

# As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. 
# So that I can find the least common multiple (L.C.M.) of my inputs.

# **Acceptance Criteria:**

# * Ask user to enter the four numbers.
# * Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# * Calculate the least common multiple (L.C.M.) of four numbers
# * Use gcd function in module of math


from math import gcd

while True:
    try:
        print('Enter 4 numbers.')
        a, b, c, d = [int(input('Input one of the number... ')) for _ in range(4)]
        print('The LCM is: ', gcd(a,b,c,d))
    except ValueError as e:
        print()
        print("Oops. Let's start again")
        print('Plese enter ONLY integer numbers!')
        print()
        continue

