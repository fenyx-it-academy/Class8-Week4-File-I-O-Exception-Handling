## Question 2
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string
import os

directory = 'letter_files'
if not os.path.exists(directory):
    os.makedirs(directory)
os.chdir('letter_files')

for letter in string.ascii_uppercase:
    with open(f'{letter}.txt', 'w', encoding='utf-8'):
        pass