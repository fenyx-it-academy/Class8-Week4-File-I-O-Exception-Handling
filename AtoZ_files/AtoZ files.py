import os

for letter in list(map(chr, range(65, 91))):  # for letter in range(A...Z)
    file_name = "%s.txt" % letter
    while not os.path.exists(file_name):
        fh = open(file_name, "w")
 
 