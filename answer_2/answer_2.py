import string
import os

current_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(current_path, "text_files")

# Create a folder if it does not exist
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
os.chdir(folder_path)

# Create a file for each letter in the alphabet
for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()
    