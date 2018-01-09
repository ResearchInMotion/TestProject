print("please enter the temperature :")

temp=int(input())

while temp>=68 and temp<=77:
    print("room temp is maintained at {} degree fah ".format(temp))
    temp=temp-1
