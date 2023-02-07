import math
 

def find_lcm(int1, int2, int3, int4):

    max_num = int1 * int2 * int3 * int4 

    for i in range(max_num, 0, -1):
        if i % num1 == 0 and i % num2 == 0 and i % num3 == 0 and i % num4 == 0:
            lcm = i
    
    print('The least common multiple of numbers is {}'.format(lcm))

try:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    num4 = int(input('Enter the fourth number: '))
    
    assert type(num1) == int  and type(num2) == int and type(num3) == int and type(num4) == int  
    
except : 
    print('Please enter an integer!')

else:
    find_lcm(num1, num2, num3, num4)
    print('The greatest common divisor of numbers is {} '.format(math.gcd(num1, num2, num3, num4)))


    

  
        
     

 