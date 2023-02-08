import string
import os
#os.chdir('C/Users/Abdulrhman Al-Tabali/Desktop/odev4')
alphabet_up = string.ascii_uppercase
alphabet_low = string.ascii_lowercase
    
alphabet_list_up=[]
alphabet_list_low=[]
for A in alphabet_up:
    alphabet_list_up.append(A)
print(alphabet_list_up)
number_up = len(alphabet_list_up)

for a in alphabet_low:
    alphabet_list_low.append(a)
print(alphabet_list_low)
number_low = len(alphabet_list_low)
with open("words1.txt", "w") as f:

    for i in range(1,number_up+1):
        f.writelines(f"{i}     {alphabet_list_up[i-1]}  \n" )
        
    
    for j in range(1,number_low+1):
        f.writelines(f"{j}     {alphabet_list_low[j-1]}  \n" )  

""" with open("words2.txt", "w") as f:
    
    for i in range(number_up):
        f.writelines( i + " " + alphabet_up[i] + "\n")
        
    
    for j in range(number_low):
        f.writelines( j + " " + alphabet_low[j] + "\n") """



    


        
    
"""  for letter in alphabet:
        for number in range(1,len(alphabet_up)):)):

    for 
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(1) """

