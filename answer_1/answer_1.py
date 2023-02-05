import string
import os

all_letters = string.ascii_lowercase + string.ascii_uppercase

current_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_path, "letters.txt")

while True:
    try:
        num_of_letters_in_line = int(input(f"How many letters in a line? [between 1 and {str(len(all_letters))}] "))
        assert num_of_letters_in_line > 0 and num_of_letters_in_line <= len(all_letters)
        break
    except ValueError:
        print("Error: not an integer!")
    except AssertionError:
        print(f"Error: not between 1 and {str(len(all_letters))}")

with open(file_path, "w") as f:
    for index, letter in enumerate(all_letters):
        f.write(letter)
        if (index + 1) % num_of_letters_in_line == 0:
            f.write("\n")
