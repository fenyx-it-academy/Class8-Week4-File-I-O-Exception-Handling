f=open("alphabet.txt","w")
latters="a b c d e f g h i j k l m n o p q r s t u v w x y z"

for i in range(26):
    latterL=latters[2*i].lower()
    latterU=latters[2*i].upper()
    f.write(str(i+1)+"-"+latterL+"\n")
    f.write(str(i+1)+"-"+latterU+"\n")
    
    
    
f.close()








