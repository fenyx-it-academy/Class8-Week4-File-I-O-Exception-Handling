from odev_4_operations import *
both_numbers=[]
while True:

    try:
        number_1 = float(input('enter a number: '))
        number_2 = float(input('enter a number: '))    
    except:
        print('invalid entry try again with a float entry')

    else: 
        both_numbers.append(number_1)
        both_numbers.append(number_2)
        print(f"the two numbers are:{both_numbers}")

        
        print(f'The subtraction is :{cikar(number_1, number_2)}')
        print(f'The summation is :{toplam(number_1, number_2)}')
        print(f'The division is :{bol(number_1, number_2)}')
        print(f'The multiplication multiplication :{carpi(number_1, number_2)}')
        both_numbers=[]
    son_cevap=input('do you want to continue? y/n : ')

    if son_cevap == 'y':
        continue
    break 
    


