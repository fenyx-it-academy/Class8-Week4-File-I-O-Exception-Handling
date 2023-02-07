# Question 3
# LCM question:
try:
    numbers = list(map(int,input('enter four numbers for calculating LCM: ').strip().split())) #Enter the numbers here with spaces between them
    numbers.sort(reverse = True)
    numbers
    from math import gcd      # importing the 'gcd' function from the 'math' module of math to calculate the greatest common divisor
    lcm = 1
    for n in numbers:
     lcm = lcm*n//gcd(lcm, n)  # Calculating the least common multiple (L.C.M.) of the numbers
     gcd()
    print("The least common multiple (L.C.M.) of your four numbers is: ", lcm)
except:
    print("Invalid input Error: Pleass enter integer numbers.")         # warnning the user for Nan or non numerical inputs
finally:
    print("It is done.")