### Question 1
"""Letters for each line
Write a Python program to create a file where all letters of English 
alphabet(uppercase and lowercase both) are listed by specified number of letters on each line.
"""

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def letters_file_line(n):
    
    with open("alphabet.txt", "w") as f:
        for i, letter in enumerate(letters):
            f.write(letter)
            if (i + 1) % n == 0:
                f.write("\n")

letters_file_line(4)