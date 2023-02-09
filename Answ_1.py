## Letters for each line

# Write a Python program to create a file where 
# all letters of English alphabet(uppercase and lowercase both) 
# are listed by specified number of letters on each line.

import string

with open('letters_file.txt', 'w') as f:
    letters=string.ascii_letters
    for i,letter in enumerate(letters,1):
        f.write(f'{i} {letter}\n') #on every line write number and letter
       
