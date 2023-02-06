import math


def lcm(*numbers):
    ''' A recursive function to find the least common multiple of a list of numbers. '''
    if len(numbers) == 2:
        # the LCM of two numbers: LCM(a, b) = a * b / gcd(a, b)
        return int(numbers[0] * numbers[1]/ math.gcd(numbers[0], numbers[1]))
    else:
        # the LCM of the first number and the LCM of the rest of the numbers
        return lcm(numbers[0], lcm(*numbers[1:]))


numbers = []
# ask the user to enter 4 numbers, only accept integers
while len(numbers) < 4:
    try:
        numbers.append(int(input("Enter a number: ")))
    except ValueError:
        print("Error: Not a number! Try again.")

# calculate the least common multiple of the 4 numbers
print(f"L.C.M of {numbers} is: {lcm(*numbers)}")
