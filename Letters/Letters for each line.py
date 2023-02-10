import os

row_len = int(input("How many copy :"))
try:
    f = open("letters.txt","w", encoding = 'utf-8')
    for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        f.write(letter*row_len+'\n')
finally:
        f.close()