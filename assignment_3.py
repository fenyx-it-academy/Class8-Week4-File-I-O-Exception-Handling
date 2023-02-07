
from math import gcd
def lcm_numbers(*numbers):
    """A function that accepts any size of numbers
     and calculates lcm of the numbers according to:
     lcm(a,b,c.....n) = lcm(lcm(a,b),c,d........n)"""
    if len(numbers)==2:
       return numbers[0] * numbers[1] // gcd(numbers[0], numbers[1])
    else:
        # since the argument passed to the function is a tuple, 
        # we need to change it in to list first to modify it.
        list_numbers = [] 
        for i in numbers:
         list_numbers.append(i)
        # x holds always the lcm of a two number
        x = lcm_numbers(list_numbers[0],list_numbers[1])
        list_numbers.pop(0)
        list_numbers.pop(0)
        list_numbers.insert(0,x)
        return lcm_numbers(*list_numbers)   
       
numbers = input('Enter numbers separated by space\n').split(" ")
try:
 numbers = [int(i) for i in numbers]
 if len(numbers) == 1:
    raise ArithmeticError ("Error! the lcm of one number is the number itself")
except ValueError as e:
    print(e)
except ArithmeticError as e:
    print(e)
else:
 lcm_result = lcm_numbers(*numbers)
 print(lcm_result)
