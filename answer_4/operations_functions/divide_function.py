from decimal import DivisionByZero
import math

def divide(a, b):
    try:
        return math.ceil(a / b)
    except ZeroDivisionError:
        return "Cannot divide by zero"
        