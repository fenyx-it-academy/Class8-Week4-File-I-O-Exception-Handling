import string
char = list(string.ascii_uppercase)
for i in range(len(char)):
   open(f"{char[i]}.txt", 'x')
