#Division

from math import ceil

def divis (n_1,n_2):
   try:
        div= n_1/n_2
   except ZeroDivisionError:
         print('Sorry, it is not possible!')
   return ceil(div)