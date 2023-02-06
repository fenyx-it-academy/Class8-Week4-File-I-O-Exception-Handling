import Question4_MisCalcAdd 
import Question4_MisCalcMulti
import Question4_MisCalcSubs
import Question4_MisCalcDiv2
import math

def inputNum(i):
    while(True):
        try:
            userInput=input(f"enter number {i}: ")
            num=float(userInput)
            return num
        except KeyboardInterrupt:
            return
        except:
            print("please enter a valid number")


num1=inputNum("1")
num2=inputNum("2")
while(True):
    try:
        userInput=input(f"enter operation \"+-*/\" : ")
        if (str(userInput) in "+-*/"):
            operator=userInput
            break
        raise Exception("Sorry, operation is not valid")
    except KeyboardInterrupt:
        break
    except:
        print("please enter a valid operation")

print(num1,num2,operator)






if operator=="+":
    result=Question4_MisCalcAdd.addNums(num1,num2)

if operator=="-":
    result=Question4_MisCalcSubs.subsNums(num1,num2)

if operator=="*":
    result=Question4_MisCalcMulti.multiNums(num1,num2)
    
if operator=="/":
    result=Question4_MisCalcDiv2.divNums2(num1,num2)

    
print(f"Result is : {math.ceil(result)}" )




            