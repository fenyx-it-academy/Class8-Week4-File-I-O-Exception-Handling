"""Question 2
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt."""

import string, os  # import string and os.path 

""" First define a function file_generaters which generates a text file for each letter of the uppercase alphabet. """

def file_generaters():
    """if a directory named "letters" exists and 
    creates it if it doesn't using the os.makedirs function."""
    
    if not os.path.exists("letters"): 
        os.makedirs("letters") 
        
    """This for loop will for each leter in the upercase alphabet, defined by string.ascii_uppercase, the code 
    creates a text file with the name of the letter and writes to the letters as its contents using the with statement
    and the open functiion. """ 
    
    for letter in string.ascii_uppercase:
        
        with open(letter + ".txt", "w") as f:
            f.writelines(letter)
file_generaters() # function is called to generate the file names
