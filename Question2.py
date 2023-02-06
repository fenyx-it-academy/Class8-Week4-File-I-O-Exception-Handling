latters="a b c d e f g h i j k l m n o p q r s t u v w x y z"

for i in range(26):
    filename=latters[i*2].upper()+".txt"
    f=open(filename,"w")
    f.close()
    