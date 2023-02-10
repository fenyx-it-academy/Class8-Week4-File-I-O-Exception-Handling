import math

numbers = []
while len(numbers)!=4:
    try:
        numbers.append(int(input(f"input {len(numbers)+1}. of 4 integer for l.c.m. calculation : ")))
        pass
    except:
        print("Enter an integer")
lcm_=  math.lcm(*numbers)
print(f"least common multiple of {numbers} = {lcm_}")