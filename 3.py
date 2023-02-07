""" As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. So that I can find the least common multiple (L.C.M.) of my inputs.

**Acceptance Criteria:**

* Ask user to enter the four numbers.
* Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
* Calculate the least common multiple (L.C.M.) of four numbers
* Use gcd function in module of math
 """

from math import gcd
from functools import reduce
import math


def calc_GCD (n1, n2):
    
    return (n1 * n2) // math.gcd(n1, n2)

def calc_LCM (*args): 

    return reduce(calc_GCD, args) # using recursion with reduce()



try:

    n_one = int(input("enter number 1: "))
    n_two = int(input("enter number 2: "))
    n_three = int(input("enter number 3: "))
    n_four =  int(input("enter number 4: "))

except ValueError :

  print ("You used a non numerical input!")

else:

    #gcd = math.gcd( math.gcd(n_one, n_two) , math.gcd(n_three, n_four) ) 
    #print (gcd)

    lcm = calc_LCM ( n_one , n_two , n_three , n_four )

    print ("the least common multiple (L.C.M.) is: " , end="")
    print (lcm)



  # for testing - 12 15 75 32 . LCM = 2400






