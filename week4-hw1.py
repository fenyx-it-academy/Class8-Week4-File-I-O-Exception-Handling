from string import ascii_lowercase
from string import ascii_uppercase
num = list(range(1,27))
import csv
 
lower = list(ascii_lowercase)
upper = list(ascii_uppercase)

f_zip = list(zip(num, lower, upper)) 

print(f_zip)

with open("abc.txt", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(f_zip)   
    

f.close()



 

     
