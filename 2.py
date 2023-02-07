# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.


import string

def create_files_A_to_Z () :
    
    A_to_Z  = string.ascii_uppercase

    for x in A_to_Z :
        #print (x)
        with open(x + ".txt", "w") as f:
            f.writelines ("")


create_files_A_to_Z()

