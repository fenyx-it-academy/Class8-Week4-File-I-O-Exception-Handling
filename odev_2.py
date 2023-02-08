import string
import os
#os.chdir('C/Users/Abdulrhman Al-Tabali/Desktop/odev4')
alphabet_up = string.ascii_uppercase
#alphabet_low = string.ascii_lowercase
    
alphabet_list_up=[]
#alphabet_list_low=[]
for A in alphabet_up:
    alphabet_list_up.append(A)
print(alphabet_list_up)
number_up = len(alphabet_list_up)

for i in range(number_up):
    with open(f'{alphabet_list_up[i]}.txt','w') as f:
        f.write(alphabet_list_up[i])
