print("Enter First Number:")
num1=int(input())
print("Enter Sceond Number:")
num2=int(input())
print("Enter the Operator:")
opr=input()

if(opr=='+'):
    if((num1==56) and (num2==9)):
        print("Addition is: 77")
    else:
        print("Addition is:",num1+num2)
elif(opr=='-'):
    print("Minus is:",num1-num2)
elif (opr == '*'):
    print("Multification is:", num1 * num2)
elif (opr == '/'):
    print("Division is:", num1 / num2)
else:
    print("Operator is invalid")


