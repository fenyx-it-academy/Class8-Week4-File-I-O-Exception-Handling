from string import ascii_uppercase

list = []

for i in ascii_uppercase:
    list.append(i+'.txt')

for j in list:
    f = open(j, 'a')
    f.close()

 

