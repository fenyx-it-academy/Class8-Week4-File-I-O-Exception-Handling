import math
numbers=[]
try:
    for i in range(4):
        digit = int(input("Enter a number: "))
        numbers.append(digit)
        


except:
        print("invalid entry Please enter a number")


else:
    print(f'the numbers entered are: {numbers}')
    print(f'the least common multiple of the digits is: {math.lcm(numbers[0],numbers[1],numbers[2],numbers[3])}')
    print(f'the gcd is: {math.gcd(numbers[0],numbers[1],numbers[2],numbers[3])}')
    
    
