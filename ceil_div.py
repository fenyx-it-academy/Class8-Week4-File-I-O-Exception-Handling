#  Division
from math import ceil
def division(number_1, number_2):
    try:
       div = number_1 / number_2
    except ZeroDivisionError as e:
       return e
    else:
     return ceil(div)