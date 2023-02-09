## LCM

# As a user, I want to use a program which can calculate the least common 
# multiple (L.C.M.) of four numbers. So that I can find the 
# least common multiple (L.C.M.) of my inputs.

# **Acceptance Criteria:**

# * Ask user to enter the four numbers.
# * Use try/except blocks to verify input entries and warn the user 
# for Nan or non numerical inputs.
# * Calculate the least common multiple (L.C.M.) of four numbers
# * Use gcd function in module of math

import sys #import module sys to get a type of exception
from math import  lcm #import lcm 



print('Enter 4 numbers.')
try:
   a,b,c,d = list(map(int, input('Numbers - ').split())) #input numbers
    # print(a,c,d)
except ValueError as e: #to verify input entries
         print()
         print('Plese enter integer numbers!')
         print('Try again!')
   # Calculate the least common multiple (L.C.M.) of four numbers 
   # use lcm (not gcd) function!   
print('least common multiple (L.C.M.) of four numbers',lcm(a,b,c,d))

    
