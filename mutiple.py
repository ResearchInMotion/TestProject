print("please enter a number : ")

number = input()
number2=int(number)

if(number2%7==0):
    print("numbr is divisble by 7")
    if(number2%14==0):
        print("number is divisble by 14")
    else:
        print("number is divisble by 3 , but not with 7 ")



#if number2 % 7 is 0:
  #print("number is divisble by 7")
  #if number2 % 14 is 0:
      #print("number is divisble by 14")
  #else:
      #print("number is divisble by 7 but not with 14")