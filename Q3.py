from math import gcd
from functools import reduce


def lcm_function(list):
    return reduce(lambda a, b: a * b // gcd(a, b), list)


list = []
for i in range(1, 5):
    try:
        num = int(input(f"Enter number {i} : "))
        num != None
        list.append(num)

    except ValueError:
        print("Value can't be empty or non numerical")
        exit()

print(list)
result = lcm_function(list)
print("The L.C.M is :", result)
