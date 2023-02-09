
while True:
    try:
        num1,num2,num3,num4=[int(input('Enter an integer')) for i in range(4)]
        i=1
        while True:
            i+=1
            if i%num1==0 and i%num2==0 and i%num3==0 and i%num4==0:
                print(i)
                break
    except:
        print("Invalid input. Please enter integer numbers.")