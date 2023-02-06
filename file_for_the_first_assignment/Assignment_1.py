## Question 1 
with open("C:/Users/sande/Documents/GitHub/Class8-Week4-File-I-O-Exception-Handling/file_for_the_first_assignment/English_letter.txt","w") as f : 
    for i in range(65,91) : 
        upper_case_letters = chr(i)
        lower_case_letters = upper_case_letters.lower()
        f.write(upper_case_letters)
        f.write(lower_case_letters)
        f.write('\t')
        f.write('\n')