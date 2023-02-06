# num1=int(input("enter number 1: "))
# num2=int(input("enter number 2: "))
# num3=int(input("enter number 3: "))
# num4=int(input("enter number 4: "))

# num1=4
# num2=5
# num3=6
# num4=7
import math


def inputNum(i):
    while(True):
        try:
            num=int(input(f"enter number {i}: "))
            return num
        except KeyboardInterrupt:
            return
        except:
            print("please enter a valid number")

numbers=[]
for i in range(1,5):
    numbers.append(inputNum(i))


LCM=math.lcm(numbers[0],numbers[1],numbers[2],numbers[3])
print("LCM is the 4 number is:", LCM)



