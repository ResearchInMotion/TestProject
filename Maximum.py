print("Enter the first number")
firstNumber=int(input())

print("Enter the second number")
secondNumber=int(input())

def maximum(Number1 , Number2):
    if(Number1>Number2):
        print("Number one is greater")
    elif(Number1<Number2):
        print("Number two is greater")
    else:
        print("both are same")

maximum(firstNumber ,secondNumber )