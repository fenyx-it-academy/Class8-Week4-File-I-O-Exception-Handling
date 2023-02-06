# Assignment week 4, question 1
import string

capital_letters = string.ascii_uppercase
lwoer_case_letters = string.ascii_lowercase


def letters_with_specific_numbers(n):
    """
    This function creates a file where all letters
    of English alphabet(uppercase and lowercase both)
    are listed by specified number of letters on each line.
    """
    lst = []
    with open("q1.txt", "w") as f:
        for i in range(0, len(capital_letters), n):
            letter = capital_letters[i : i + n]
            lst.append(letter)

        f.write("\n".join(lst))
        f.write("\n")
        lst2 = []
        for i in range(0, len(lwoer_case_letters), n):
            letter = lwoer_case_letters[i : i + n]
            lst2.append(letter)

        f.write("\n".join(lst2))


letters_with_specific_numbers(3)
