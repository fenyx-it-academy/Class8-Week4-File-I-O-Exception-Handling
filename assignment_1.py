import string


def write_alphabet(per_line):
    """A function that accepts the number of letters per line
    and writes all English alphabet letters (upper and lower) in to a
    file name letters.txt. it works for any number of letters per line"""
    with open("letters.txt", "w") as write_file:
        all_letters = string.ascii_letters  # all alphabets given to all_letters
        size = len(all_letters)
        for letters in range(0, size - per_line + 1, per_line):
            for index in range(letters, letters + per_line):
                write_file.write(all_letters[index])
            write_file.write("\n")
        # this if clause is for perline which is not divident of 52
        if size % per_line != 0:
            write_file.write(all_letters[-(size % per_line) :])


# the function will be called here
try:
    number_letters = int(input("Enter the number of letters per line:........ "))
    if number_letters <= 0:
        raise RuntimeError("Error: please enter a number > 0 ")
except ValueError as e:
    print(e)
except RuntimeError as e:
    print(e)
else:
    write_alphabet(number_letters)
