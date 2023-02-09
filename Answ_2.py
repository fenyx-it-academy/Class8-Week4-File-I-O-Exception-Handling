## Question 2

# Write a Python program to generate 26 text files named A.txt, B.txt, 
# and so on up to Z.txt.

import string
import os

os.mkdir('Letters') #make a directory for alphabet files

os.chdir('Letters') #make the 'Letters' a current directory

letters=string.ascii_uppercase #make a sequence of uppercase letters.
for letter in letters: # loop to creat lettersnamed files
    with open(f'{letter}.txt','x'):
        pass