from math import ceil
def addition(number_1, number_2):
    add = number_1 + number_2
    return ceil(add)
def subtruction(number_1, number_2):
    sub = number_1 - number_2
    return ceil(sub)
def multiplication(number_1, number_2):
    mul = number_1 * number_2
    return ceil(mul)
def division(number_1, number_2):
    try:
       divide = number_1 / number_2
    except ZeroDivisionError as e:
       return e
    else:
     return ceil(divide)