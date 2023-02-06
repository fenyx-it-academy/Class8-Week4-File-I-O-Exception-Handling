## Letters for each line
# Write a Python program to create a file where all letters of English alphabet(uppercase and lowercase both) 
# are listed by specified number of letters on each line.

import string

with open("Numbered letters.txt", 'w', encoding='utf-8') as f:
    for i, letter in enumerate(string.ascii_letters, 1):
        f.write(f'{i}\t{letter}\n')