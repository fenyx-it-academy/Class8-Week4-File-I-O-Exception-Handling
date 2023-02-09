import string

with open("Numbered letters.txt", 'w', encoding='utf-8') as f:
    for i, letter in enumerate(string.ascii_letters, 1):
        f.write(f'{i}\t{letter}\n')