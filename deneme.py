import string
index = 1


def numbered_letters():
with open("alphabet.txt", "w") as f:
    for value in string.ascii_letters:
        f.write(f'{index}  {value}\n')
        index += 1
        
