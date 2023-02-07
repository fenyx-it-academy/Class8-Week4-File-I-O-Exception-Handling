# Question 1
import string

def letters_4_line(n):
   with open("letters4line.txt", "w") as f:
       alphabet1 = string.ascii_uppercase # choosing upper case
       alphabet2 = string.ascii_lowercase  # choosing lower case
       letters_ubb_low = [alphabet1[i:i + n]+ alphabet2[i:i + n] + "\n" for i in range(0, len(alphabet1), n)]
       f.writelines(letters_ubb_low)
letters_4_line(1)