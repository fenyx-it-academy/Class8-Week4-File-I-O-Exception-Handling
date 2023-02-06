## Question 3 
## LCM

import sys
import math 
list1 = []
while 1 : 
    try:
        number = input("please enter the numbers : " )
        int(number)
        list1.append(int(number))

        if len(list1) == 4 : 
           break
    except ValueError : 
        print("its not number please try again :( ")
print("The numbers that you enter it  : " ,list1)
print("The LCM for the numbers that you enter it : ",math.lcm(list1[0],list1[1],list1[2],list1[3]))
gcd_number = math.gcd(list1[0],list1[1],list1[2],list1[3])
print("The GCD for the numbers that you enter it : ",gcd_number)
