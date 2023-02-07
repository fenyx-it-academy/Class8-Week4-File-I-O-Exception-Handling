import string

n = int(input("Enter the number of letters in each line:"))
with open("letters.txt", "w") as f:
    alphabet = string.ascii_letters
    for i in range(0, len(alphabet), n):
        letters = [alphabet[i:i + n] + "\n"]
        f.writelines(letters)
