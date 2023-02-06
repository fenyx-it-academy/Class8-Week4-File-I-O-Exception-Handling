# Assignment week_4, question 2
import string
import os


# store the text files in q2 alphabet directory
if os.path.exists("Q2 alphabet file"):
    pass
else:
    os.mkdir("Q2 alphabet file")

# change the directory to \q2 alphabet file
os.chdir("Q2 alphabet file")
letters = string.ascii_uppercase

for i in letters:
    with open(i + ".txt", "w") as f:
        f.write(i)
