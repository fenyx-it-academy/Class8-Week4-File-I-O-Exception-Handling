import os
import string
for char in string.ascii_uppercase:
 with open(f"{char}.txt", 'w'):
     pass
# the following code helps us to delete all the files created.
delete = input("do you want to delete the files?......." )
if delete in ["yes","Yes","y","Y"]:
 for char in string.ascii_uppercase:
   os.remove(f"{char}.txt" )