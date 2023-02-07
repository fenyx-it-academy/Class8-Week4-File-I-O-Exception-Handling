# Write a Python program to create a file where all letters of English alphabet(uppercase and lowercase both) are listed by specified number of letters on each line.


import string

def print_alphabet_per_line(n) :

   with open("letters.txt", "w") as f:

    alphabet = string.ascii_uppercase + string.ascii_lowercase

    for i in range(0, len(alphabet), n) :

        letters = alphabet[i:i + n] + "\n"
        f.writelines(letters)




print_alphabet_per_line(5)



