import string
import os

current_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(current_path, "text_files")

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
os.chdir(folder_path)

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()
    